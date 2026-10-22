# site — `site` — Site-specific configuration hook

# Site, Smtpd

## Overview

Covers: site — Site-specific configuration hook; smtpd — SMTP Server.

## site — Site-specific configuration hook

### `site` — Site-specific configuration hook

**Source code:** [Lib/site.py](https://github.com/python/cpython/tree/3.14/Lib/site.py)

---

**This module is automatically imported during initialization.** You can prevent that automatic import by passing the interpreter's [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) option.

As a rule, importing this module tacks site-specific paths onto the module search path and places [callables](https://docs.python.org/3.14/library/constants.html#site-consts) — [`help()`](https://docs.python.org/3.14/library/functions.html#help) among them — into the built-in namespace. The [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) startup option for Python halts that behavior, though, allowing the module to be imported safely without any automatic tweaks to the search path or additions to the builtins. When you want the customary site-specific additions applied deliberately, invoke the `main()` function.

Changed in version 3.3: Formerly, importing the module would set off path manipulation even under [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S).

The process begins by assembling as many as four directories, each from a head piece and a tail piece. The head piece draws on `sys.prefix` and `sys.exec_prefix`, with any empty heads passed over. The tail piece is first the empty string and then `lib/site-packages` (under Windows) or `lib/python*X.Y[t]*/site-packages` (under Unix and macOS). (That optional “t” suffix marks the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) and gets appended whenever `"t"` appears in the [`sys.abiflags`](https://docs.python.org/3.14/library/sys.html#sys.abiflags) constant.) For every distinct head-tail pairing, it checks whether the result names a directory that exists; when it does, the path joins `sys.path` and is then scanned for configuration files.

Changed in version 3.5: The “site-python” directory is no longer supported.

Changed in version 3.13: Under Unix, a [Free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) Python installation is recognized by the “t” suffix on its version-specific directory name, for example `lib/python3.13t/`.

Changed in version 3.14: Keeping [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) current within [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) is no longer the job of `site`. That work has shifted into [path initialization](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init). Consequently, inside [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) the values of `sys.prefix` and `sys.exec_prefix` no longer hinge on `site` setup and thus remain untouched by [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S).

While operating inside a [virtual environment](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments), the `pyvenv.cfg` file located in [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) gets examined for site-specific settings. Should the `include-system-site-packages` key be present and hold `true` (matched case-insensitively), the system-level prefixes are searched for site-packages; without that, they are left out.

Any file named in the pattern `*name*.pth` that sits in one of the four directories named earlier counts as a path configuration file; the lines it holds are extra entries — one per line — destined for `sys.path`. Entries that don't exist never make it onto `sys.path`, and nothing verifies whether an entry points at a directory or a file. The same entry is never placed on `sys.path` twice. Empty lines and lines that open with `#` get passed over. Lines beginning with `import` (trailed by a space or tab) are run.

Note

Every Python startup runs an executable line found in a `.pth` file, whether or not the module in question ends up being used at all. For that reason its footprint ought to stay as small as possible. Executable lines are meant chiefly to render the relevant module(s) importable (bringing in 3rd-party import hooks, tweaking `PATH`, and so on). Anything else by way of initialization belongs at the module's genuine import, whenever that occurs. Capping a code fragment at one line is an intentional choice meant to discourage tucking anything more elaborate in here.

Changed in version 3.13: Decoding of `.pth` files now tries UTF-8 first, falling back to the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) only when that attempt fails.

Imagine, for instance, that `sys.prefix` and `sys.exec_prefix` both equal `/usr/local`. In that case the Python X.Y library lands in `/usr/local/lib/python*X.Y*`. Say it carries a subdirectory `/usr/local/lib/python*X.Y*/site-packages` containing three nested directories — `foo`, `bar`, and `spam` — plus a pair of path configuration files, `foo.pth` and `bar.pth`. Take `foo.pth` to hold this:

```none
# foo package configuration

foo
bar
bletch

```

and `bar.pth` contains:

```none
# bar package configuration

bar

```

These version-specific directories then get appended to `sys.path`, following this sequence:

```none
/usr/local/lib/pythonX.Y/site-packages/bar
/usr/local/lib/pythonX.Y/site-packages/foo

```

Observe that `bletch` is left out since it has no actual existence; the `bar` directory lands ahead of the `foo` directory because `bar.pth` sorts alphabetically before `foo.pth`; and `spam` drops away because neither path configuration file refers to it.

[Subject index](INDEX.md) · [Continue](sitecustomize.md)
