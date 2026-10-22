# ensurepip — Module API

### Module API

For use from code, `ensurepip` makes two functions available:

`ensurepip.version()`

Gives back a string naming the pip version on hand — the one that will be installed when an environment is bootstrapped.

`ensurepip.bootstrap(*root=None*, *upgrade=False*, *user=False*, *altinstall=False*, *default_pip=False*, *verbosity=0*)`

Bootstraps `pip` into either the current environment or one you nominate.

*root* names an alternative root directory that the install should be made relative to. With *root* left as `None`, the install falls back to the default location for the current environment.

*upgrade* says whether an existing, older `pip` should be brought up to the available version.

*user* says whether to follow the user scheme in place of a global install.

Out of the box the `pipX` and `pipX.Y` scripts are installed, with X.Y denoting Python's current version.

Set *altinstall* and `pipX` is *not* installed.

Set *default_pip* and `pip` is installed on top of the two ordinary scripts.

Setting *altinstall* together with *default_pip* raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

*verbosity* dictates how much output the bootstrapping operation sends to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ensurepip.bootstrap` with argument `root`.

Note

Bootstrapping leaves side effects on both `sys.path` and `os.environ`. Running the command line interface inside a subprocess instead lets you steer clear of those side effects.

Note

Bootstrapping can pull in extra modules that `pip` depends on, yet other software ought not take for granted that those dependencies will always be there by default, since a later `pip` release might drop them.

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Owning module, declaration or section: ensurepip](ensurepip-bootstrapping-the-pip-installer.md)
