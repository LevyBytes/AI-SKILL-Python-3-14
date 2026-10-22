# profile: `profile.run()`, `profile.runctx()`

### `profile` and `cProfile` Module Reference

Both the `profile` and `cProfile` modules provide the following functions:

 profile.run(*command*, *filename=None*, *sort=-1*)

This function accepts a single argument that can be passed to the [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) function, plus an optional file name. In every case the routine runs:

```python
exec(command, __main__.__dict__, __main__.__dict__)

```

and collects profiling statistics from running it. When no file name is supplied, the function automatically builds a `Stats` instance and prints a brief profiling report. When the sort value is given, it is passed along to that `Stats` instance to govern how the results get ordered.

 profile.runctx(*command*, *globals*, *locals*, *filename=None*, *sort=-1*)

This function resembles `run()`, with extra arguments that provide the globals and locals mappings for the *command* string. The routine runs:

```python
exec(command, globals, locals)

```

and collects profiling statistics just as the `run()` function above does.

[Subject index](INDEX.md) · [Previous](instant-user-s-manual-contract-s-sort-order.md) · [Continue](profile-profile-class-to-profile-profile-runcall.md)
