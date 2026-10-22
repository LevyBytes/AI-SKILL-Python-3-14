# __main__ — Packaging Considerations

### Packaging Considerations

A common way to build command-line tools is to register `main` functions as entry points for console scripts. With that arrangement, [pip](https://pip.pypa.io/) drops the function call into a template script, feeding the `main` return value into [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit). As an illustration:

```python
sys.exit(main())

```

Because the `main` call sits inside [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit), your function is expected to hand back something `sys.exit()` will accept — generally an integer or `None` (the latter returned implicitly whenever your function lacks a return statement).

If we adopt this convention up front ourselves, our module behaves identically whether launched directly (that is, `python echo.py`) or later shipped as a console script entry-point inside a pip-installable package.

Take special care, in particular, when your `main` function returns strings. [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) reads a string argument as a failure message, leaving your program with an exit code of `1` to signal failure and writing the string to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). The earlier `echo.py` example demonstrates the `sys.exit(main())` convention in action.

See also

[Python Packaging User Guide](https://packaging.python.org/) gathers tutorials and references covering how to distribute and install Python packages using modern tooling.

[Subject index](INDEX.md) · [Previous](idiomatic-usage.md) · [Continue](main-py-in-python-packages.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md)
