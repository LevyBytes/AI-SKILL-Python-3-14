# -I

-I

Launch Python in isolated mode. Doing so also brings along the `-E`, `-P` and `-s` options.

Under isolated mode, [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) includes neither the script's directory nor the user's site-packages directory. Every `PYTHON*` environment variable is disregarded too. Additional limits may be applied to keep the user from injecting malicious code.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous source section](interactive-after-script.md) · [Following source section](optimize-assertions.md)
