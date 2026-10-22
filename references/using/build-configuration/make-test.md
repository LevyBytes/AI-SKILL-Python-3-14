# 3.4.3.7. make test

#### 3.4.3.7. make test

Build the `all` target, then run the Python test suite under the `--fast-ci` option while leaving the GUI tests out. Variables:

- `TESTOPTS`: extra command-line options handed to regrtest.

- `TESTPYTHONOPTS`: extra command-line options handed to Python.

- `TESTTIMEOUT`: the timeout in seconds (default: 10 minutes).

[Subject index](INDEX.md) · [Previous source section](make-install.md) · [Following source section](make-ci.md)
