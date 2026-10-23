# What's New In Python 3.10 / distutils - platform, shutil, subprocess, sysconfig

### distutils

Slated for removal in Python 3.12, the whole `distutils` package is now deprecated. The third-party `setuptools` and `packaging` packages have already taken over its package-build specification role completely, and a good deal of its other widely used APIs turn up elsewhere across the standard library (for example, [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform), [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil), [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) or [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig)). Nobody intends to port any remaining functionality out of `distutils`, so applications leaning on other functions ought to plan on keeping private copies of that code. See [**PEP 632**](https://peps.python.org/pep-0632/) for the discussion.

Deprecated back in Python 3.8, the `bdist_wininst` command has now been dropped. For shipping binary packages on Windows, the `bdist_wheel` command is the new recommendation. (Contributed by Victor Stinner in [bpo-42802](https://bugs.python.org/issue?@action=redirect&bpo=42802).)

[Subject index](INDEX.md) · [Previous source section](dataclasses-keyword-only-fields.md) · [Next source section](doctest.md) · [Release/subject declaration](summary-release-highlights.md)
