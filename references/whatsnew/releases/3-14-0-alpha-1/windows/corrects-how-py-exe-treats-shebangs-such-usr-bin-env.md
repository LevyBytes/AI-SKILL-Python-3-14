# Python 3.14.0 alpha 1 / windows / corrects how py exe treats shebangs such usr bin env

[gh-119070](https://github.com/python/cpython/issues/119070): Corrects how `py.exe` treats shebangs such as `/usr/bin/env python3.12`, which formerly resolved to `python3.exe` rather than `python3.12.exe`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
