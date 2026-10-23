# What's New In Python 3.13 / PEP 594: Remove "dead batteries" from the standard library - base64, mimetypes, shlex, subprocess

- [standard-crypt](https://pypi.org/project/standard-crypt/) and [deprecated-crypt-alternative](https://pypi.org/project/deprecated-crypt-alternative/): Use the redistribution of `crypt` and reimplementation of `_crypt` libraries from PyPI.

- `imghdr`: Reach instead for the [filetype](https://pypi.org/project/filetype/), [puremagic](https://pypi.org/project/puremagic/), or [python-magic](https://pypi.org/project/python-magic/) libraries. As one case, the `puremagic.what()` function stands in for the `imghdr.what()` function across every file format that `imghdr` once handled.

  - [standard-imghdr](https://pypi.org/project/standard-imghdr/): Use the redistribution of `imghdr` library from PyPI.

- `mailcap`: Reach for the [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) module in its place.

  - [standard-mailcap](https://pypi.org/project/standard-mailcap/): Use the redistribution of `mailcap` library from PyPI.

- `msilib`

- `nis`

- `nntplib`: Reach for the [pynntp](https://pypi.org/project/pynntp/) library from PyPI in its place.

  - [standard-nntplib](https://pypi.org/project/standard-nntplib/): Use the redistribution of `nntplib` library from PyPI.

- `ossaudiodev`: To play audio, turn to the [pygame](https://pypi.org/project/pygame/) library from PyPI in its place.

- `pipes`: Reach for the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module in its place. Swap [`shlex.quote()`](https://docs.python.org/3.14/library/shlex.html#shlex.quote) in for the undocumented `pipes.quote` function.

  - [standard-pipes](https://pypi.org/project/standard-pipes/): Use the redistribution of `pipes` library from PyPI.

- `sndhdr`: Reach instead for the [filetype](https://pypi.org/project/filetype/), [puremagic](https://pypi.org/project/puremagic/), or [python-magic](https://pypi.org/project/python-magic/) libraries.

  - [standard-sndhdr](https://pypi.org/project/standard-sndhdr/): Use the redistribution of `sndhdr` library from PyPI.

- `spwd`: Reach for the [python-pam](https://pypi.org/project/python-pam/) library from PyPI in its place.

- `sunau`

  - [standard-sunau](https://pypi.org/project/standard-sunau/): Use the redistribution of `sunau` library from PyPI.

- `telnetlib`, Reach for the [telnetlib3](https://pypi.org/project/telnetlib3/) or [Exscript](https://pypi.org/project/Exscript/) libraries from PyPI in its place.

  - [standard-telnetlib](https://pypi.org/project/standard-telnetlib/): Use the redistribution of `telnetlib` library from PyPI.

- `uu`: Reach for the [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) module in its place, a present-day alternative.

  - [standard-uu](https://pypi.org/project/standard-uu/): Use the redistribution of `uu` library from PyPI.

[Subject index](INDEX.md) · [Previous source section](removed-modules-and-standard-library-replacements.md) · [Next source section](pep-594-remove-dead-batteries-from-the-standard-library.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](removed-modules-and-standard-library-replacements.md)
