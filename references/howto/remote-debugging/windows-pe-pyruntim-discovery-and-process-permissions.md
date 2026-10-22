# Windows PE PyRuntim discovery and process permissions

Windows (PE)

Here is how to find the `PyRuntime` structure under Windows:

1.

Employ the ToolHelp API to list every module loaded within the target process. The functions used for this include [CreateToolhelp32Snapshot](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot), [Module32First](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-module32first), and [Module32Next](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-module32next).

2.

Find the module that matches `python.exe` or `python*XY*.dll` — where `X` and `Y` stand for the major and minor version numbers of the Python release — and note down its base address.

3.

Track down the `PyRuntim` section. Because the PE format caps section names at 8 characters (specified by `IMAGE_SIZEOF_SHORT_NAME`), the original `PyRuntime` name gets truncated. The `PyRuntime` structure is contained in this section.

4.

Obtain the section's relative virtual address (RVA) and combine it with the module's base address.

What follows is a sample implementation:

```python
def find_py_runtime_windows(pid: int) -> int:
    # Step 1: Try to find the Python executable in memory
    binary_path, base_address = find_loaded_module(
        pid, name_contains="python"
    )

    # Step 2: Fallback to shared pythonXY.dll if the executable is not
    # found
    if binary_path is None:
        binary_path, base_address = find_loaded_module(
            pid, name_contains="python3"
        )

    # Step 3: Parse PE section headers to get the RVA of the PyRuntime
    # section. The section name appears as "PyRuntim" due to the
    # 8-character limit defined by the PE format (IMAGE_SIZEOF_SHORT_NAME).
    section_rva = parse_pe_section_offset(binary_path, "PyRuntim")

    # Step 4: Compute PyRuntime address in memory
    return base_address + section_rva

```

Under Windows, reaching another process's memory means using Windows API functions — such as `CreateToolhelp32Snapshot()` and `Module32First()/Module32Next()` — to enumerate the loaded modules. A handle for accessing the target process's memory space comes from the `OpenProcess()` function, which then makes memory operations through `ReadProcessMemory()` possible.

You can inspect the process memory by enumerating loaded modules until the Python binary or DLL turns up. Once located, its PE headers have to be parsed to pinpoint the `PyRuntime` structure.

Sections are how the PE format groups its code along with its data. A section bearing the name "PyRuntim" (shortened from "PyRuntime" because PE limits names to 8 characters) is where the `PyRuntime` structure resides. Working out the actual runtime address means first deriving the module's base address from the module entry, then finding our target section within the PE headers. To get the final address, the base address is combined with the section's virtual address drawn from the PE section headers.

Keep in mind that, under Windows, reaching the memory of another process usually calls for suitable privileges — be it administrative access or having `SeDebugPrivilege` conferred on the debugging process.

[Subject index](INDEX.md) · [PyRuntime discovery model and Linux ELF implementation](pyruntime-discovery-model-and-linux-elf-implementation.md) · [macOS Mach-O discovery, memory APIs and privileges](macos-mach-o-discovery-memory-apis-and-privileges.md) · [Previous source context](macos-mach-o-discovery-memory-apis-and-privileges.md) · [Following source context](reading-py-debugoffsets.md)
