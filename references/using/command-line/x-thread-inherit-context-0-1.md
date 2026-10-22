# -X thread_inherit_context=*0,1*

- `-X thread_inherit_context=*0,1*` makes [`Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread), as its default, adopt a copy of the context belonging to whoever called `Thread.start()` at launch time. If not, threads begin with an empty context. When left unset, this option's value falls back to `1` on free-threaded builds and `0` everywhere else. Refer also to `PYTHON_THREAD_INHERIT_CONTEXT`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](x-gil-0-1.md) · [Following source section](x-context-aware-warnings-0-1.md)
