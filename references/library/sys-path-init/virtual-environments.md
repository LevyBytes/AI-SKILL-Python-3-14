# sys.monitoring — Virtual Environments

### Virtual Environments

Virtual environments drop a `pyvenv.cfg` file into their prefix, which makes [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) refer to them in place of the base installation.

The base installation's `prefix` and `exec_prefix` values are available at [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix) and [`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix).

Besides serving as a marker that flags virtual environments, `pyvenv.cfg` can also be used to configure the [`site`](https://docs.python.org/3.14/library/site.html#module-site) initialization. Have a look at `site`'s [virtual environments documentation](https://docs.python.org/3.14/library/site.html#site-virtual-environments-configuration).

Note

[`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) overrides the `pyvenv.cfg` detection.

Note

"Virtual environments" could be built in other ways too; this documentation speaks to implementations grounded in the `pyvenv.cfg` mechanism, such as [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv). The bulk of virtual environment implementations track the model `venv` established, though there may be exotic ones that stray from it.

[Subject index](INDEX.md) · [Previous](the-initialization-of-the-sys-path-module-search-path.md) · [Continue](pth-files.md)
