# readline — `readline` — GNU readline interface

# Readline, Removed, Reprlib

## Overview

Covers: readline — GNU readline interface; Removed Modules; reprlib — Alternate repr() implementation.

## readline — GNU readline interface

### `readline` — GNU readline interface

---

A collection of functions for completion and for reading or writing history files from the Python interpreter is supplied by the `readline` module. You may call it on its own, or through the [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) module, which handles completion of Python identifiers at the interactive prompt. Any settings applied through this module influence the behaviour of the interpreter's interactive prompt as well as the prompts that the built-in [`input()`](https://docs.python.org/3.14/library/functions.html#input) function presents.

You can configure Readline keybindings through an initialization file, usually `.inputrc` within your home directory. Consult [Readline Init File](https://tiswww.cwru.edu/php/chet/readline/rluserman.html#Readline-Init-File) in the GNU Readline manual for details on that file's format and permitted constructs, plus what the Readline library can do in general.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

There is no support for this module on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or on [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

This counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should it be absent from your build of CPython, consult documentation from whoever supplied your copy (in other words, your distributor). Distributors themselves should review [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Note

Rather than GNU readline, the underlying Readline library API may be backed by the `editline` (`libedit`) library. The `readline` module on macOS works out which library is in play during run time.

`editline` uses a configuration file that differs from the one GNU readline expects. When you load configuration strings programmatically, `backend` lets you find out which library is active.

On macOS, if your setup relies on `editline`/`libedit` readline emulation, the initialization file in your home directory carries the name `.editrc`. As an illustration, placing the lines below in `~/.editrc` enables *vi* keybindings together with TAB completion:

```python
python:bind -v
python:bind ^I rl_complete

```

Be aware too that history file formats can vary between libraries. After you change the underlying library, history files you already have may stop working.

 readline.backend

The name identifying which underlying Readline library is active, either `"readline"` or `"editline"`.

Added in version 3.13.

[Subject index](INDEX.md) · [Continue](readline-parse-and-bind-to-readline-read-init-file.md)
