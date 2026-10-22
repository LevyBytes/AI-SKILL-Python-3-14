# Python 3.9.0 alpha 5 / build / subprocess

[bpo-39763](https://bugs.python.org/issue?@action=redirect&bpo=39763): Should the `subprocess` module be unavailable, setup.py now falls back on a minimal implementation of the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module: this happens before the required C extension modules get built.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
