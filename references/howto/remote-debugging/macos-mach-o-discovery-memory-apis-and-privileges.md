# macOS Mach-O discovery, memory APIs and privileges

macOS (Mach-O)

Here is how to find the `PyRuntime` structure under macOS:

1.

Invoke `task_for_pid()` so as to obtain the `mach_port_t` task port for the target process. APIs such as `mach_vm_read_overwrite` and `mach_vm_region` need this handle to read memory.

2.

Sweep the memory regions to identify the one holding the Python executable or `libpython`.

3.

Read the on-disk binary file and parse the Mach-O headers to find the section called `PyRuntime` inside the `__DATA` segment. Since symbol names on macOS get an automatic underscore prefix, the `PyRuntime` symbol shows up as `_PyRuntime` within the symbol table, although the section name stays unaffected.

What follows is a sample implementation:

```python
def find_py_runtime_macos(pid: int) -> int:
    # Step 1: Get access to the process's memory
    handle = get_memory_access_handle(pid)

    # Step 2: Try to find the Python executable in memory
    binary_path, base_address = find_mapped_binary(
        handle, name_contains="python"
    )

    # Step 3: Fallback to libpython if the executable is not found
    if binary_path is None:
        binary_path, base_address = find_mapped_binary(
            handle, name_contains="libpython"
        )

    # Step 4: Parse Mach-O headers to get __DATA,__PyRuntime section offset
    section_offset = parse_macho_section_offset(
        binary_path, "__DATA", "__PyRuntime"
    )

    # Step 5: Compute the PyRuntime address in memory
    return base_address + section_offset

```

Reaching another process's memory under macOS calls for Mach-O specific APIs together with the corresponding file formats. The opening move is to acquire a `task_port` handle by way of `task_for_pid()`, which yields access to the target process's memory space. Memory operations through APIs like `mach_vm_read_overwrite()` are made possible by this handle.

`mach_vm_region()` lets you inspect the process memory by sweeping across the virtual memory space, whereas `proc_regionfilename()` assists in determining which binary files occupy each memory region. Upon finding the Python binary or library, its Mach-O headers must be parsed to pinpoint the `PyRuntime` structure.

Within the Mach-O format, code and data are arranged into segments and sections. The `PyRuntime` structure resides in a section called `__PyRuntime` that sits inside the `__DATA` segment. Computing the actual runtime address entails first locating the `__TEXT` segment, which acts as the binary's base address, and then finding the `__DATA` segment that holds our target section. To get the final address, the base address is combined with the relevant section offsets taken from the Mach-O headers.

Be aware that reaching another process's memory under macOS generally demands elevated privileges — either root access or special security entitlements conferred on the debugging process.

[Subject index](INDEX.md) · [PyRuntime discovery model and Linux ELF implementation](pyruntime-discovery-model-and-linux-elf-implementation.md) · [Windows PE PyRuntim discovery and process permissions](windows-pe-pyruntim-discovery-and-process-permissions.md) · [Previous source context](pyruntime-discovery-model-and-linux-elf-implementation.md) · [Following source context](windows-pe-pyruntim-discovery-and-process-permissions.md)
