# cmd — `cmd` — Support for line-oriented command interpreters

## cmd — Support for line-oriented command interpreters

### `cmd` — Support for line-oriented command interpreters

**Source code:** [Lib/cmd.py](https://github.com/python/cpython/tree/3.14/Lib/cmd.py)

---

The `Cmd` class offers a lightweight framework for authoring line-oriented command interpreters. Such interpreters frequently serve as test harnesses, administrative utilities, and prototypes destined to be dressed up later in a richer interface.

 *class *cmd.Cmd(*completekey='tab'*, *stdin=None*, *stdout=None*)

A `Cmd` instance, or an instance of a subclass, is a line-oriented interpreter framework. Instantiating `Cmd` on its own serves no real purpose; instead it shines as a superclass for an interpreter class you write yourself, so that your class picks up `Cmd`'s methods and bundles in action methods.

The optional argument *completekey* is the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) name for a completion key, defaulting to Tab. As long as *completekey* is not [`None`](https://docs.python.org/3.14/library/constants.html#None) and `readline` is present, command completion happens automatically.

The default value `'tab'` gets special handling so that it points at the Tab key on every [`readline.backend`](https://docs.python.org/3.14/library/readline.html#readline.backend). Concretely, when `readline.backend` is `editline`, `Cmd` substitutes `'^I'` for `'tab'`. Other values, note, receive no such handling and may function only with one particular backend.

The optional arguments *stdin* and *stdout* name the input and output file objects the Cmd instance or subclass instance will draw on for input and output. Left unspecified, they fall back to [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

Should you want a particular *stdin* honored, be sure to set the instance's `use_rawinput` attribute to `False`; otherwise *stdin* is disregarded.

Changed in version 3.13: `completekey='tab'` is replaced by `'^I'` for `editline`.

[Subject index](INDEX.md) · [Continue](cmd-cmdloop-to-cmd-intro.md)
