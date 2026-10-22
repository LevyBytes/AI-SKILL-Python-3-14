# Writing control information

### Writing control information

After a valid `PyThreadState` structure has been pinpointed, the debugger is free to change control fields inside it so as to schedule the running of a given Python script. The interpreter inspects these control fields at intervals, and when they are set properly, they bring about the execution of remote code at a safe point within the evaluation loop.

Communication between the debugger and the interpreter relies on a `_PyRemoteDebuggerSupport` structure held within each `PyThreadState`. Where its fields are located is dictated by the `_Py_DebugOffsets` structure, and they comprise the following:

- `debugger_script_path`: A buffer of fixed size that stores the full path of a Python source file (`.py`). At the moment execution is triggered, this file has to be reachable and readable by the target process.

- `debugger_pending_call`: A flag of integer type. Setting it to `1` informs the interpreter that a script stands ready to run.

- `eval_breaker`: A field the interpreter inspects while running. Setting bit 5 (`_PY_EVAL_PLEASE_STOP_BIT`, value `1U << 5`) in this field makes the interpreter pause and check for debugger activity.

To finish the injection, the debugger has to carry out the following steps:

1.

Write the complete script path into the `debugger_script_path` buffer.

2.

Set `debugger_pending_call` to a value of `1`.

3.

Read the current `eval_breaker` value, set bit 5 (`_PY_EVAL_PLEASE_STOP_BIT`) in it, and write the modified value back. Doing so signals the interpreter to look for debugger activity.

What follows is a sample implementation:

```python
def inject_script(
    pid: int,
    thread_state_addr: int,
    debug_offsets: DebugOffsets,
    script_path: str
) -> None:
    # Compute the base offset of _PyRemoteDebuggerSupport
    support_base = (
        thread_state_addr +
        debug_offsets.debugger_support.remote_debugger_support
    )

    # Step 1: Write the script path into debugger_script_path
    script_path_ptr = (
        support_base +
        debug_offsets.debugger_support.debugger_script_path
    )
    write_string(pid, script_path_ptr, script_path)

    # Step 2: Set debugger_pending_call to 1
    pending_ptr = (
        support_base +
        debug_offsets.debugger_support.debugger_pending_call
    )
    write_int(pid, pending_ptr, 1)

    # Step 3: Set _PY_EVAL_PLEASE_STOP_BIT (bit 5, value 1 << 5) in
    # eval_breaker
    eval_breaker_ptr = (
        thread_state_addr +
        debug_offsets.debugger_support.eval_breaker
    )
    breaker = read_int(pid, eval_breaker_ptr)
    breaker |= (1 << 5)
    write_int(pid, eval_breaker_ptr, breaker)

```

With these fields set, the debugger is free to resume the process (where it had been suspended). At its next safe evaluation point, the interpreter will handle the request, load the script off disk, and run it.

Keeping the script file present and reachable by the target process throughout execution is the debugger's responsibility.

Note

[Subject index](INDEX.md) · [Following source continuation](writing-control-information-continuation.md) · [Previous source context](lookup-by-native-thread-id-and-injection-prerequisite.md)
