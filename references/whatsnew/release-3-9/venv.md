# What's New In Python 3.9 / venv - venv

### venv

The activation scripts shipped with [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) now handle their prompt customization the same way across the board, always relying on whatever `__VENV_PROMPT__` holds. Earlier, certain scripts used `__VENV_PROMPT__` unconditionally, some referenced it only when it happened to be defined (which was the usual situation), and one relied on `__VENV_NAME__` instead. (Contributed by Brett Cannon in [bpo-37663](https://bugs.python.org/issue?@action=redirect&bpo=37663).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](xml.md) · [Release/subject declaration](summary-release-highlights.md)
