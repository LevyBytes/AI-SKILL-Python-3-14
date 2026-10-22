# A per-interpreter GIL

### A per-interpreter GIL

Added in version 3.12.

By going through `Py_NewInterpreterFromConfig()` you are able to stand up a sub-interpreter wholly walled off from the others, GIL of its own included. Isolation's chief payoff is that an interpreter like this runs Python code neither held up by the other interpreters nor holding any of them up. Consequently one lone Python process genuinely exploits several CPU cores while executing Python code. Isolation likewise nudges you toward a concurrency style apart from merely leaning on threads. (Consult [**PEP 554**](https://peps.python.org/pep-0554/) along with [**PEP 684**](https://peps.python.org/pep-0684/).)

Working with an isolated interpreter demands care to keep that isolation intact. Above all that rules out sharing any object or mutable state absent thread-safety assurances. Because of the refcount, even objects that are otherwise immutable (`None` or `(1, 5)`, say) usually cannot be shared. A plain albeit less-efficient workaround wraps a global lock around every use of a particular state (or object). As an alternative, objects that are immutable in practice (integers or strings, for example) can be rendered safe despite their refcounts by turning them [immortal](https://docs.python.org/3.14/glossary.html#term-immortal). Indeed this very treatment already covers the builtin singletons, the small integers, and a range of further builtin objects.

Keep isolation intact and you gain genuine multi-core computing free of the headaches free-threading brings. Let isolation slip and free-threading's full fallout lands on you, races and crashes that defy debugging among them.

Beyond all that, a leading difficulty in running several isolated interpreters lies in passing data between them both safely (without rupturing isolation) and efficiently. So far neither the runtime nor the stdlib ships a standard way to do this. Down the road a stdlib module could ease the burden of holding isolation together and surface capable tools for relaying (and sharing) data among interpreters.

[Subject index](INDEX.md) · [Previous source contract](py-newinterpreterfromconfig-to-py-endinterpreter.md) · [Following source contract](bugs-and-caveats.md)
