# What's new in Python 3.14 / Default interactive shell

### Default interactive shell

- Python syntax is now highlighted by the default [interactive](https://docs.python.org/3.14/glossary.html#term-interactive) shell. This is on by default, except when [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) or some other environment variable that turns off colour has been set. Consult [Controlling color](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color) for the specifics.

Aiming for solid contrast, the default color theme for syntax highlighting draws solely on the 4-bit VGA standard ANSI color codes so that compatibility stays maximal. An experimental API `_colorize.set_theme()` lets you customize the theme. You may invoke it interactively or inside the [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) script. Be aware that this function carries no stability guarantees and could change or disappear.

(Contributed by Łukasz Langa in [gh-131507](https://github.com/python/cpython/issues/131507).)

- Import auto-completion is now handled by the default [interactive](https://docs.python.org/3.14/glossary.html#term-interactive) shell. As a result, entering `import co` and hitting &lt;Tab&gt; will propose modules whose names begin with `co`. In the same way, entering `from concurrent import i` will propose submodules of `concurrent` that begin with `i`. Be aware that completing module attributes is not yet handled. (Contributed by Tomas Roun in [gh-69605](https://github.com/python/cpython/issues/69605).)

[Subject index](INDEX.md) · [Previous source section](garbage-collection.md) · [Next source section](new-modules.md) · [Release/subject declaration](summary-release-highlights.md)
