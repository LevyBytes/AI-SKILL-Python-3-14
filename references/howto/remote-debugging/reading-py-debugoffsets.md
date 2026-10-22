# Reading _Py_DebugOffsets

### Reading _Py_DebugOffsets

With the address of the `PyRuntime` structure now known, the following task is to read the `_Py_DebugOffsets` structure that sits at the start of the `PyRuntime` block.

The version-specific field offsets supplied by this structure are required for reading interpreter and thread state memory safely. Because these offsets differ across CPython versions, they have to be validated before use to confirm compatibility.

Use these steps to read and validate the debug offsets:

1.

Read memory out of the target process beginning at the `PyRuntime` address, spanning as many bytes as the `_Py_DebugOffsets` structure occupies. That structure sits at the very beginning of the `PyRuntime` memory block. Defined in CPython's internal headers, its layout holds constant within a given minor version but is subject to change across major versions.

2.

Confirm that the structure holds valid data:

  - The expected debug marker must be matched by the `cookie` field.

  - The `version` field has to match the version of the Python interpreter that the debugger is using.

  - Should either the debugger or the target process be running a pre-release build (an alpha, beta, or release candidate, for example), the versions are required to match precisely.

  - In both the debugger and the target process, the `free_threaded` field must carry an identical value.

3.

When the structure is valid, the offsets within it can serve to locate fields in memory. Should any check not pass, the debugger ought to abort the operation so it does not read memory in the wrong format.

What follows is a sample implementation that reads and validates `_Py_DebugOffsets`:

```python
def read_debug_offsets(pid: int, py_runtime_addr: int) -> DebugOffsets:
    # Step 1: Read memory from the target process at the PyRuntime address
    data = read_process_memory(
        pid, address=py_runtime_addr, size=DEBUG_OFFSETS_SIZE
    )

    # Step 2: Deserialize the raw bytes into a _Py_DebugOffsets structure
    debug_offsets = parse_debug_offsets(data)

    # Step 3: Validate the contents of the structure
    if debug_offsets.cookie != EXPECTED_COOKIE:
        raise RuntimeError("Invalid or missing debug cookie")
    if debug_offsets.version != LOCAL_PYTHON_VERSION:
        raise RuntimeError(
            "Mismatch between caller and target Python versions"
        )
    if debug_offsets.free_threaded != LOCAL_FREE_THREADED:
        raise RuntimeError("Mismatch in free-threaded configuration")

    return debug_offsets

```

Warning

**Process suspension recommended**

So as to head off race conditions and keep memory consistent, suspending the target process before you carry out any operation that reads or writes internal interpreter state is strongly advised. While running normally, the Python runtime may mutate interpreter data structures concurrently — creating or tearing down threads, for instance. The upshot can be invalid memory reads or writes.

A debugger can halt execution by attaching to the process via `ptrace` or by dispatching a `SIGSTOP` signal. Only after the debugger-side memory operations have finished should execution be resumed.

Note

Certain tools — profilers or sampling-based debuggers, say — may work on a running process without suspending it. Under those circumstances, the tools have to be deliberately built to cope with memory that is partially updated or inconsistent. For most debugger implementations, though, suspending the process stays the safest and most robust route.

[Subject index](INDEX.md) · [Previous source context](windows-pe-pyruntim-discovery-and-process-permissions.md) · [Following source context](interpreter-thread-state-traversal-and-main-thread-lookup.md)
