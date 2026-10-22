# ensurepip — Command-line interface

### Command-line interface

You launch the command line interface by way of the interpreter's `-m` switch.

At its barest, the call looks like:

```python
python -m ensurepip

```

Run that way, it installs `pip` when `pip` isn't there yet and stays idle otherwise. To make certain the `pip` you have is no older than the build `ensurepip` carries, tack on the `--upgrade` option:

```python
python -m ensurepip --upgrade

```

Out of the box, `pip` lands in the active virtual environment when one is running, or otherwise in the system site packages where no virtual environment is active. You steer where it goes with a further pair of command line options:

 --root &lt;dir&gt;

Puts `pip` in place relative to the root directory you name, instead of relative to the root of whatever virtual environment is active or the default root belonging to the current Python installation.

 --user

Puts `pip` in the user site packages directory rather than installing it globally for the current Python installation; this option is barred while a virtual environment is active.

Out of the box, the `pipX` and `pipX.Y` scripts get installed, where X.Y denotes the Python version that ran `ensurepip`. Which scripts end up installed is governed by a further pair of command line options:

 --altinstall

Ask for an alternate installation and the `pipX` script is *not* installed.

 --default-pip

Ask for a “default pip” installation and the `pip` script gets installed on top of the two ordinary scripts.

Supplying both script-selection options at once raises an exception.

[Subject index](INDEX.md) · [Previous](ensurepip-bootstrapping-the-pip-installer.md) · [Continue](ensurepip-version-to-ensurepip-bootstrap.md) · [Owning module, declaration or section: ensurepip](ensurepip-bootstrapping-the-pip-installer.md)
