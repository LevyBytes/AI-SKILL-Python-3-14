# sysconfig — Prefix scheme

### Prefix scheme

The “prefix scheme” earns its keep when you want one Python installation to carry out the build/install (that is, to run the setup script) while the modules themselves land in the third-party module directory of some other Python installation (or something resembling one). If that strikes you as a little odd, it is — which is exactly why the user and home schemes are presented first. Even so, at least two recognized situations make the prefix scheme worthwhile.

To begin with, note that plenty of Linux distributions place Python under `/usr` instead of the more customary `/usr/local`. That choice is perfectly reasonable, because in those cases Python counts as part of “the system” rather than a local add-on. Yet when you install Python modules from source, you most likely want them deposited in `/usr/local/lib/python2.*X*` rather than `/usr/lib/python2.*X*`.

A second scenario is a network filesystem on which the name used for writing to a remote directory differs from the one used for reading it: as an example, the Python interpreter reached as `/usr/local/bin/python` might look for modules in `/usr/local/lib/python2.*X*`, while those modules would need to be installed to, say, `/mnt/*@server*/export/lib/python2.*X*`.

[Subject index](INDEX.md) · [Previous](posix-home.md) · [Continue](posix-prefix.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)
