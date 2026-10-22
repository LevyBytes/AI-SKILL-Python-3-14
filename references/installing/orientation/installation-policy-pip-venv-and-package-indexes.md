# Installation scope, institutional policies, pip, venv, PyPI, and PyPA

# Installing

### Installing Python modules

Being a widely used open source effort, Python enjoys a lively community of contributors and users who likewise release their own software for fellow Python developers under open-source licensing.

That arrangement lets Python users share and work together productively, drawing on fixes that others have already worked out for everyday (and occasionally quite unusual!) problems, while also having the chance to add their own contributions back to the shared pool.

The focus here is the installation side of things. If instead you want guidance on building and distributing Python projects of your own, see the [Python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Note

If you work somewhere corporate or institutional, keep in mind that plenty of organisations set their own rules about consuming and contributing to open source software. Factor those rules in whenever you reach for the distribution and installation tooling that ships with Python.

### Key terms

- **pip** is the recommended installer tool. The Python binary installers bundle it by default.

- A *virtual environment* is a partially isolated Python setup that lets packages be installed for one specific application's use instead of across the whole system.

- `venv` is the go-to tool for building virtual environments. By default it puts **pip** into every virtual environment it makes.

- `virtualenv` is an outside, third-party option that came before `venv`.

- The [Python Package Index (PyPI)](https://pypi.org) is an open repository holding open source licensed packages that any Python user can pull from.

- The [Python Packaging Authority](https://www.pypa.io/) is the body of developers and documentation writers who look after and advance the standard packaging tools together with the related metadata and file-format standards. They keep up an assortment of tools, docs, and issue trackers over on [GitHub](https://github.com/pypa).

Changed in version 3.5: `venv` is now the recommended choice for building virtual environments.

See also

[Python Packaging User Guide: Creating and using virtual environments](https://packaging.python.org/installing/#creating-virtual-environments)

[Subject index](INDEX.md) · [Next source section](install-version-pin-upgrade-and-use-virtual-environments.md)
