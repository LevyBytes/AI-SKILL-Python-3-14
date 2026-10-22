# Python 3.11.0 alpha 2 / core and builtins / extensions declaring they rely global state done setting m size

[bpo-44050](https://bugs.python.org/issue?@action=redirect&bpo=44050): Extensions declaring that they rely on global state (done by setting `m_size` to -1) may once more be loaded across multiple interpreters. This restores the way Python 3.8 behaved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
