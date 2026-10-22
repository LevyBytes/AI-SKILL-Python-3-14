# concurrent.interpreters.Interpreter: `is_running()`, `close()`, `prepare_main()`, `exec()`, `call()`, `call_in_thread()`

`is_running()`

Give back `True` when the interpreter is right then running code in its `__main__` module, and `False` if not.

`close()`

Wind the interpreter down and tear it apart.

`prepare_main(*ns=None*, ***kwargs*)`

Attach objects within the interpreter’s `__main__` module.

A few objects are shared outright and a few are copied cheaply, but the bulk travel through [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle). Refer to “Sharing” Objects.

`exec(*code*, */*, *dedent=True*)`

Execute the supplied source code inside the interpreter (within the current thread).

`call(*callable*, */*, **args*, ***kwargs*)`

Give back the outcome of running the supplied function inside the interpreter (within the current thread).

`call_in_thread(*callable*, */*, **args*, ***kwargs*)`

Execute the supplied function inside the interpreter (within a fresh thread).

[Subject index](INDEX.md) · [Previous](concurrent-interpreters-interpreter-class.md) · [Continue](interpreter-sharing-exceptions.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md) · [Owning module, declaration or section: concurrent.interpreters.Interpreter](concurrent-interpreters-interpreter-class.md) · [Owning module, declaration or section: Interpreter objects](concurrent-interpreters-interpreter-class.md)
