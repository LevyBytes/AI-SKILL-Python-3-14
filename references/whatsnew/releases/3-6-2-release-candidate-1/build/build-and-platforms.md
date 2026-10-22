# Python 3.6.2 release candidate 1 / build / build and platforms

[bpo-29941](https://bugs.python.org/issue?@action=redirect&bpo=29941): Introduce a `--with-assertions` configure flag that turns on C `assert()` checks explicitly. The default is off. `--with-pydebug` implies `--with-assertions`.

[bpo-29243](https://bugs.python.org/issue?@action=redirect&bpo=29243): Stop Python from being needlessly rebuilt during `make test`, `make install` and certain other make targets whenever the configuration uses `--enable-optimizations`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
