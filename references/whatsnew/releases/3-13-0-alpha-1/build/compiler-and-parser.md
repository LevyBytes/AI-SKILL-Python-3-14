# Python 3.13.0 alpha 1 / build / compiler and parser

[gh-105481](https://github.com/python/cpython/issues/105481): Took out the make target `regen-opcode-targets` and folded its work into `regen-opcode`, which redoes the bulk of that calculation. This trims down the build code and cuts code duplication.

[gh-106118](https://github.com/python/cpython/issues/106118): Repaired compilation on platforms lacking `O_CLOEXEC`. The problem came in with Python 3.12b1 over at [gh-103295](https://github.com/python/cpython/issues/103295). Erlend Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
