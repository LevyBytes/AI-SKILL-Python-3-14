# Interpreter/thread-state traversal and main-thread lookup

### Locating the interpreter and thread state

Ahead of injecting and running code in a remote Python process, the debugger has to pick a thread in which the execution will be scheduled. The reason is that the control fields driving remote code injection reside in the `_PyRemoteDebuggerSupport` structure, which is embedded inside a `PyThreadState` object. The debugger alters these fields to ask for injected scripts to run.

A thread executing within a Python interpreter is represented by the `PyThreadState` structure. It keeps the thread's evaluation context and holds the fields needed for coordinating with the debugger. Finding a valid `PyThreadState` is, for that reason, an essential precondition for kicking off execution remotely.

Usually a thread gets chosen according to its role or ID. The main thread serves in most situations, though certain tools may go after a particular thread using its native thread ID. After the target thread has been picked, the debugger has to find both the interpreter and the related thread state structures within memory.

Here is how the relevant internal structures are defined:

- An isolated Python interpreter instance is represented by `PyInterpreterState`. Every interpreter keeps its own collection of imported modules, built-in state, and thread state list. Even though most Python applications run with a single interpreter, CPython permits multiple interpreters within one process.

- A thread running inside an interpreter is represented by `PyThreadState`. It holds execution state along with the control fields the debugger uses.

To find a thread:

1.

Apply the offset `runtime_state.interpreters_head` to get the address of the first interpreter inside the `PyRuntime` structure. This serves as the entry point into the linked list of active interpreters.

2.

Apply the offset `interpreter_state.threads_main` to reach the main thread state tied to the chosen interpreter. As a rule this is the most dependable thread to target.

3.

Optionally, apply the offset `interpreter_state.threads_head` to traverse the linked list of every thread state. Within each `PyThreadState` structure sits a `native_thread_id` field, which may be checked against a target thread ID to pin down a specific thread.

4.

After a valid `PyThreadState` has been found, its address is usable in subsequent steps of the protocol, including writing debugger control fields and scheduling execution.

What follows is a sample implementation that finds the main thread state:

```python
def find_main_thread_state(
    pid: int, py_runtime_addr: int, debug_offsets: DebugOffsets,
) -> int:
    # Step 1: Read interpreters_head from PyRuntime
    interp_head_ptr = (
        py_runtime_addr + debug_offsets.runtime_state.interpreters_head
    )
    interp_addr = read_pointer(pid, interp_head_ptr)
    if interp_addr == 0:
        raise RuntimeError("No interpreter found in the target process")

    # Step 2: Read the threads_main pointer from the interpreter
    threads_main_ptr = (
        interp_addr + debug_offsets.interpreter_state.threads_main
    )
    thread_state_addr = read_pointer(pid, threads_main_ptr)
    if thread_state_addr == 0:
        raise RuntimeError("Main thread state is not available")

    return thread_state_addr

```

[Subject index](INDEX.md) · [Lookup by native thread ID and injection prerequisite](lookup-by-native-thread-id-and-injection-prerequisite.md) · [Previous source context](reading-py-debugoffsets.md) · [Following source context](lookup-by-native-thread-id-and-injection-prerequisite.md)
