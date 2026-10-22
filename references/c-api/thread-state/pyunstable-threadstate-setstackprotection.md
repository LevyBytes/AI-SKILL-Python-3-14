# int PyUnstable_ThreadState_SetStackProtection(PyThreadState *tstate, void *stack_start_addr, size_t stack_size)

int PyUnstable_ThreadState_SetStackProtection(PyThreadState *tstate, void *stack_start_addr, size_t stack_size)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Assign both the starting address and the size of the stack-protection region belonging to a given Python thread state.

When it works, return `0`; when it fails, raise an exception and hand back `-1`.

To keep C code from running away, CPython provides [recursion control](https://docs.python.org/3.14/c-api/exceptions.html#recursion): once it detects that the machine's execution stack is nearing an overflow, it throws [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError). The [`Py_EnterRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_EnterRecursiveCall) function is one illustration of this. Doing so requires knowing where the running thread's stack sits, a detail the runtime usually obtains from the operating system. Should that stack be swapped out — say, through a coroutine-style context switch such as the Boost library's `boost::context` — you are obliged to invoke `PyUnstable_ThreadState_SetStackProtection()` so that CPython learns of the new arrangement.

You may invoke `PyUnstable_ThreadState_SetStackProtection()` on either side of the stack swap — before it or after it. Just refrain from issuing any other Python C API in the interval separating that invocation from the swap itself.

To reverse this, consult `PyUnstable_ThreadState_ResetStackProtection()`.

Added in version 3.15.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pythreadstate-new-to-pythreadstate-entertracing.md) · [Following source contract](pythreadstate-leavetracing.md) · [Following source contract](stack-protection-and-thread-lock-apis.md)
