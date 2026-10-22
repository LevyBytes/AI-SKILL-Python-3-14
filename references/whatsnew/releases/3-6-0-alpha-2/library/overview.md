# Python 3.6.0 alpha 2 / library / overview

### Library

- Commented out the socket (SO_REUSEPORT) and posix (O_SHLOCK, O_EXLOCK) constants that the API exposes but GNU/Hurd never implements. At runtime they would fail to work regardless.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
