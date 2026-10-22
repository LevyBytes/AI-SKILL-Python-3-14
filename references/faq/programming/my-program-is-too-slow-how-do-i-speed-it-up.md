# My program is too slow. How do I speed it up?

### Performance

### My program is too slow. How do I speed it up?

In general, that's a hard one. To begin, here are some points worth keeping in mind before you go any deeper:

- How code performs differs from one Python implementation to the next. The focus of this FAQ is [CPython](https://docs.python.org/3.14/glossary.html#term-CPython).

- Behaviour can shift between operating systems, particularly where I/O or multi-threading is concerned.

- Before you try to optimize any code, you ought always to locate the hot spots in your program *first* (consult the [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile) module).

- Putting benchmark scripts together lets you iterate rapidly as you hunt for improvements (consult the [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module).

- It is strongly advised to maintain solid code coverage (via unit testing or some other method) before you risk introducing regressions buried inside elaborate optimizations.

With that said, plenty of tricks exist for accelerating Python code. Below are some broad principles that carry you a good distance toward attaining acceptable performance:

- Speeding up your algorithms (or swapping in faster ones) can deliver far greater gains than scattering micro-optimization tricks throughout your code.

- Pick the right data structures. Review the documentation for the [Built-in Types](https://docs.python.org/3.14/library/stdtypes.html#bltin-types) and the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.

- Whenever the standard library offers a primitive for a task, it is probably (though not certainly) faster than anything you might devise yourself. That goes doubly for primitives coded in C, like builtins and certain extension types. For instance, be sure to reach for either the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) built-in method or the corresponding [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function when sorting (and the [Sorting Techniques](https://docs.python.org/3.14/howto/sorting.html#sortinghowto) page shows examples of somewhat advanced usage).

- Abstractions have a way of introducing indirections that make the interpreter labor harder. Where the layers of indirection exceed the volume of useful work being done, your program runs slower. Steer clear of excessive abstraction, above all in the shape of tiny functions or methods (which often hurt readability too).

If you've hit the ceiling of what pure Python permits, there are tools to carry you further. For instance, [Cython](https://cython.org) can compile a lightly modified form of Python code into a C extension, and works across many different platforms. By leveraging compilation (along with optional type annotations), Cython can make your code far faster than it runs when interpreted. And if you trust your C programming abilities, you can even [write a C extension module](https://docs.python.org/3.14/extending/index.html#extending-index) on your own.

See also

The wiki page dedicated to [performance tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips).

[Subject index](INDEX.md)
