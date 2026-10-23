# venv`venv` - Creation of virtual environments

### `venv` - Creation of virtual environments

Added in version 3.3.

**Source code:** [Lib/venv/](https://github.com/python/cpython/tree/3.14/Lib/venv/)

---

With the `venv` module you can build lightweight “virtual environments”, every one carrying its own separate collection of Python packages placed inside that environment’s [`site`](https://docs.python.org/3.14/library/site.html#module-site) directories. Each virtual environment is layered over a Python installation that already exists — referred to as the environment’s “base” Python — and, by default, stays isolated from whatever the base environment holds, leaving available only what you deliberately install into the virtual environment itself. For further details consult [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) along with the [virtual environments documentation](https://docs.python.org/3.14/library/site.html#site-virtual-environments-configuration) of `site`.

While you operate inside a virtual environment, the usual installer programs — [pip](https://pypi.org/project/pip/) being the typical one — drop Python packages straight into that virtual environment without you having to instruct them to do so.

Among other roles, a virtual environment is:

- A holder for one particular Python interpreter together with the software libraries and binaries a given project (whether a library or an application) relies on. By default these stand apart from software in separate virtual environments as well as from Python interpreters and libraries that the operating system has installed.

- Kept inside a directory: by convention called `.venv` or `venv` within the project folder, or otherwise grouped beneath a container folder meant to hold many virtual environments, for instance `~/.virtualenvs`.

- Left out of source control systems like Git.

- Treated as throwaway – wiping it out and rebuilding it from nothing ought to be easy. None of your project’s code belongs in the environment.

- Not regarded as something you move or copy – instead you simply rebuild an equivalent environment wherever you need it.

Consult [**PEP 405**](https://peps.python.org/pep-0405/) for additional background covering Python virtual environments.

See also

[Python Packaging User Guide: Creating and using virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

There is no support for this module on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or on [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

[Subject index](INDEX.md) · [Continue](creating-virtual-environments.md)
