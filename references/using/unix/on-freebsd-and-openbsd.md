# 2.1.2. On FreeBSD and OpenBSD

### 2.1.2. On FreeBSD and OpenBSD

- On FreeBSD, install the package with:

```sh
pkg install python3

```

- On OpenBSD, install the package with:

```sh
pkg_add -r python

pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz

```

As an illustration, on i386 you would fetch Python 2.5.1 like this:

```sh
pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz

```

[Subject index](INDEX.md) · [Previous source section](installing-idle.md) · [Following source section](building-python.md)
