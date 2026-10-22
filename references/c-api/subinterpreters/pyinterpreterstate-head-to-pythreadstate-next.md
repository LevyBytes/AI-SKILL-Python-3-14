# Advanced debugger support

### Advanced debugger support

The functions here are meant purely for use by advanced debugging tools.

 PyInterpreterState *PyInterpreterState_Head()

Hand back whichever interpreter state object sits first in the list holding all of them.

 PyInterpreterState *PyInterpreterState_Main()

Hand back the state object of the main interpreter.

 PyInterpreterState *PyInterpreterState_Next(PyInterpreterState *interp)

Hand back the interpreter state object that follows *interp* within the list holding all of them.

 [PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *PyInterpreterState_ThreadHead(PyInterpreterState *interp)

Hand back a pointer aimed at the leading [`PyThreadState`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) object within the thread list tied to the interpreter *interp*.

 [PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *PyThreadState_Next([PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *tstate)

Hand back the thread state object that comes after *tstate* within the list of all those tied to the same `PyInterpreterState` object.

[Subject index](INDEX.md) · [Previous source contract](pyinterpreterstate-new-to-pyinterpreterstate-delete.md)
