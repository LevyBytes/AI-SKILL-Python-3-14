# What’s New In Python 3.12 / ensurepip — ensurepip, venv

### ensurepip

- Drop the bundled setuptools wheel out of [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip), and quit installing setuptools into environments made by [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv).

`pip (>= 22.1)` has no need for setuptools to live in the environment. Packages built on `setuptools` (and on `distutils`) can still go through `pip install`, because pip supplies `setuptools` within the build environment it spins up to build a package.

`easy_install`, `pkg_resources`, `setuptools` and `distutils` no longer ship by default in environments made via `venv` or seeded through `ensurepip`, given that they belong to the `setuptools` package. Projects that depend on these at runtime should list the `setuptools` project as a dependency and install it on its own (commonly via pip).

(Contributed by Pradyun Gedam in [gh-95299](https://github.com/python/cpython/issues/95299).)

[Subject index](INDEX.md) · [Previous source section](distutils.md) · [Next source section](enum.md) · [Release/subject declaration](summary-release-highlights.md)
