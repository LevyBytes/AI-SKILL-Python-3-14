# PyRuntime discovery model and Linux ELF implementation

### Locating the PyRuntime structure

To make the `PyRuntime` structure easy for outside tools to locate at runtime, CPython positions it within a dedicated binary section. That section's name and layout differ from one platform to the next. As examples, ELF systems use `.PyRuntime`, while macOS uses `__DATA,__PyRuntime`. By inspecting the on-disk binary, tools can determine this structure's offset.

CPython's global interpreter state lives in the `PyRuntime` structure, which also opens the door to additional internal data — among them the list of interpreters, thread states, and the fields supporting debuggers.

For a debugger to interact with a remote Python process, it first has to determine where the `PyRuntime` structure sits in the target process's memory. Because the location depends on wherever the operating system mapped the binary, this address can neither be hardcoded nor derived from a symbol name.

How `PyRuntime` is found varies with the platform, yet the general sequence stays the same:

1.

Determine the base address at which the Python binary or shared library got loaded inside the target process.

2.

From the on-disk binary, find the offset of the `.PyRuntime` section.

3.

Combine the section offset with the base address to arrive at the in-memory address.

Below, the sections explain how this is accomplished on each platform that is supported, complete with sample code.

Linux (ELF)

Here is how to find the `PyRuntime` structure under Linux:

1.

Examine the process's memory map (`/proc/<pid>/maps`, for instance) to discover the address where the Python executable or `libpython` was mapped.

2.

Walk the ELF section headers within the binary to obtain the `.PyRuntime` section's offset.

3.

Combine that offset with the base address obtained in step 1 to produce the in-memory address of `PyRuntime`.

What follows is a sample implementation:

```python
def find_py_runtime_linux(pid: int) -> int:
    # Step 1: Try to find the Python executable in memory
    binary_path, base_address = find_mapped_binary(
        pid, name_contains="python"
    )

    # Step 2: Fallback to shared library if executable is not found
    if binary_path is None:
        binary_path, base_address = find_mapped_binary(
            pid, name_contains="libpython"
        )

    # Step 3: Parse ELF headers to get .PyRuntime section offset
    section_offset = parse_elf_section_offset(
        binary_path, ".PyRuntime"
    )

    # Step 4: Compute PyRuntime address in memory
    return base_address + section_offset

```

Under Linux, two principal techniques exist for reading another process's memory. One goes through the `/proc` filesystem — reading from `/proc/[pid]/mem` in particular, which grants direct access to the process's memory. The required permissions here are either matching the target process's user or holding root access. The alternative employs the `process_vm_readv()` system call, a more efficient route for copying memory across processes. The `PTRACE_PEEKTEXT` operation of ptrace can read memory too, but it is considerably slower, since it pulls only a single word at a time and entails repeated context switches between the tracer and tracee processes.

Parsing ELF sections involves reading and interpreting the structures of the ELF file format from the on-disk binary file. Inside the ELF header sits a pointer to the section header table. Every section header carries metadata describing a section — its name (kept in a separate string table), its offset, and its size, among other things. Finding a particular section such as .PyRuntime means stepping through these headers and matching against the section name. The section header subsequently yields the offset at which that section resides in the file, and that offset serves to derive the runtime address once the binary has been loaded into memory.

Further details on the ELF file format are available in the [ELF specification](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).

[Subject index](INDEX.md) · [macOS Mach-O discovery, memory APIs and privileges](macos-mach-o-discovery-memory-apis-and-privileges.md) · [Windows PE PyRuntim discovery and process permissions](windows-pe-pyruntim-discovery-and-process-permissions.md) · [Previous source context](permission-requirements.md) · [Following source context](macos-mach-o-discovery-memory-apis-and-privileges.md)
