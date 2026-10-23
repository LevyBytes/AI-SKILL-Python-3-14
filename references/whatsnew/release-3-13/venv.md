# What's New In Python 3.13 / venv - venv

### venv

- Introduce support for generating source control management (SCM) ignore files within the directory of a virtual environment. Git works out of the box. The feature is opt-in through the API, which can grow to cover further SCMs ([`EnvBuilder`](https://docs.python.org/3.14/library/venv.html#venv.EnvBuilder) and [`create()`](https://docs.python.org/3.14/library/venv.html#venv.create)), and opt-out via the CLI by passing `--without-scm-ignore-files`. (Contributed by Brett Cannon in [gh-108125](https://github.com/python/cpython/issues/108125).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](warnings.md) · [Release/subject declaration](summary-release-highlights.md)
