# Python 3.13.0 alpha 1 / library / venv

[gh-83417](https://github.com/python/cpython/issues/83417): Give venv the capability to write a `.gitignore` file so the freshly created environment ends up ignored by Git. The behavior defaults to on whenever venv runs through its CLI.

[gh-89427](https://github.com/python/cpython/issues/89427): Establish the `VIRTUAL_ENV_PROMPT` environment variable on [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) activation, even where `VIRTUAL_ENV_DISABLE_PROMPT` has been set.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
