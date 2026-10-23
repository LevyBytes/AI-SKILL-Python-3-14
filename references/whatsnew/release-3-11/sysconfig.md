# What's New In Python 3.11 / sysconfig - sysconfig, venv

### sysconfig

- A trio of fresh [installation schemes](https://docs.python.org/3.14/library/sysconfig.html#installation-paths) (*posix_venv*, *nt_venv* and *venv*) were introduced; Python applies them whenever it builds new virtual environments or executes from inside one. The opening pair (*posix_venv* and *nt_venv*) are OS-specific, one for non-Windows and one for Windows, whereas *venv* is basically an alias pointing at whichever fits the OS Python is on. Distributors downstream who tweak [`sysconfig.get_preferred_scheme()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_preferred_scheme) find this handy. To resolve paths, external code that spins up new virtual environments ought to adopt the new *venv* installation scheme, which is exactly what [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) does. (Contributed by Miro Hrončok in [bpo-45413](https://bugs.python.org/issue?@action=redirect&bpo=45413).)

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](tempfile.md) · [Release/subject declaration](summary-release-highlights.md)
