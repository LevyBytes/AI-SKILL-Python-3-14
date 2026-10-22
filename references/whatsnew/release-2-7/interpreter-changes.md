# What’s New in Python 2.7 / Interpreter Changes — http.cookies

### Interpreter Changes

There is a new environment variable, [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS), for steering warnings. Give it a string of warning settings, the same ones you would pass with the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) switch, separated by commas. (Provided by Brian Curtin; [bpo-7301](https://bugs.python.org/issue?@action=redirect&bpo=7301).)

To take one example, the setting below prints warnings on each occurrence yet converts any warning coming from the [`Cookie`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies) module into an error. (How you actually assign an environment variable depends on your operating system and shell.)

```python
export PYTHONWARNINGS=all,error:::Cookie:0

```

[Subject index](INDEX.md) · [Previous source section](file-errors-and-language-behavior.md) · [Next source section](optimizations.md) · [Release/subject declaration](the-future-for-python-2-x.md)
