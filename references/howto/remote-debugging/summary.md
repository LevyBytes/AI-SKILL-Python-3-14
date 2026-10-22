# Summary

### Summary

To push a Python script into a remote process and run it:

1.

Find where the `PyRuntime` structure sits within the target process's memory.

2.

Read out the `_Py_DebugOffsets` structure that opens `PyRuntime`, and confirm it is valid.

3.

Apply those offsets to find a valid `PyThreadState`.

4.

Store the Python script's path inside `debugger_script_path`.

5.

Switch the `debugger_pending_call` flag on by giving it `1`.

6.

Turn on `_PY_EVAL_PLEASE_STOP_BIT` within the `eval_breaker` field.

7.

Let the process continue (where it was paused). Your script then runs once the interpreter reaches its next safe evaluation point.

[Subject index](INDEX.md) · [Previous source context](writing-control-information-continuation.md) · [Following source context](security-and-threat-model.md)
