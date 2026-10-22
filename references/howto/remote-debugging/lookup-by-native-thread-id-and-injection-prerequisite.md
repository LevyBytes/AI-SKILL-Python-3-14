# Lookup by native thread ID and injection prerequisite

This next example shows how a thread can be located by its native thread ID:

```python
def find_thread_by_id(
    pid: int,
    interp_addr: int,
    debug_offsets: DebugOffsets,
    target_tid: int,
) -> int:
    # Start at threads_head and walk the linked list
    thread_ptr = read_pointer(
        pid,
        interp_addr + debug_offsets.interpreter_state.threads_head
    )

    while thread_ptr:
        native_tid_ptr = (
            thread_ptr + debug_offsets.thread_state.native_thread_id
        )
        native_tid = read_int(pid, native_tid_ptr)
        if native_tid == target_tid:
            return thread_ptr
        thread_ptr = read_pointer(
            pid,
            thread_ptr + debug_offsets.thread_state.next
        )

    raise RuntimeError("Thread with the given ID was not found")

```

Once a valid thread state is in hand, the debugger can move on to altering its control fields and scheduling execution, as the next section describes.

[Subject index](INDEX.md) · [Interpreter/thread-state traversal and main-thread lookup](interpreter-thread-state-traversal-and-main-thread-lookup.md) · [Previous source context](interpreter-thread-state-traversal-and-main-thread-lookup.md) · [Following source context](writing-control-information.md)
