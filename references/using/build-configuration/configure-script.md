# 3.2.1. configure script

### 3.2.1. configure script

Running `make regen-configure` rebuilds both the `aclocal.m4` file and the `configure` script by way of the `Tools/build/regen-configure.sh` shell script, which relies on an Ubuntu container so the tool versions stay identical and the output stays reproducible.

That container is not mandatory; you may instead run the command below directly:

```sh
autoreconf -ivf -Werror

```

Output among the generated files may vary according to the precise tool versions in play. CPython's container ships [Autoconf](https://gnu.org/software/autoconf) 2.72, `aclocal` supplied by [Automake](https://www.gnu.org/software/automake) 1.16.5, plus [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) 1.8.1.

Changed in version 3.13: Regenerating `configure` now relies on Autoconf 2.71 and aclocal 1.16.5.

Changed in version 3.14: Regenerating `configure` now relies on Autoconf 2.72.

[Subject index](INDEX.md) · [Previous source section](generated-files.md) · [Following source section](configure-options.md)
