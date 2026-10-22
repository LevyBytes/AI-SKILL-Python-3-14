# Bugs and caveats

### Bugs and caveats

Since the sub-interpreters together with the main interpreter all live inside one process, the wall separating them is imperfect — for instance, through low-level file operations such as [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close) one can meddle (by accident or on purpose) with another's open files. Owing to how extensions get shared across (sub-)interpreters, certain extensions might misbehave; the risk climbs particularly with single-phase initialization or (static) global variables in play. You can drop objects built in one sub-interpreter into a namespace of some other (sub-)interpreter; steer clear of doing so where you can.

Take particular pains not to share user-defined functions, methods, instances or classes among sub-interpreters, since the import operations those objects trigger may touch the wrong (sub-)interpreter's loaded-module dictionary. Just as crucial is steering clear of sharing any object from which the foregoing can be reached.

Bear in mind too that pairing this capability with the `PyGILState_*` APIs is touchy, because those APIs presume a one-to-one mapping of Python thread states onto OS-level threads — a presumption that sub-interpreters violate. The strong advice is that you refrain from switching sub-interpreters in between a matched pair of [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) and [`PyGILState_Release()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Release) calls. Beyond that, extensions (such as [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes)) that lean on these APIs to let Python code be invoked from threads not created by Python are likely to break once sub-interpreters enter the picture.

[Subject index](INDEX.md) · [Previous source contract](py-newinterpreterfromconfig.md) · [Following source contract](pyinterpreterstate-to-pyinterpreterstate-setevalframefunc.md)
