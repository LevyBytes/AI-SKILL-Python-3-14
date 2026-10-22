# platform — Command-line usage

### Command-line usage

You can equally run `platform` on its own through the interpreter's [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch:

```python
python -m platform [--terse] [--nonaliased] [{nonaliased,terse} ...]

```

The following options are accepted:

 --terse

Emit a terse summary of the platform. This amounts to invoking `platform.platform()` with its *terse* argument set to `True`.

 --nonaliased

Emit the platform details with no system/OS name aliasing applied. This amounts to invoking `platform.platform()` with its *aliased* argument set to `True`.

You may additionally supply one or more positional arguments (`terse`, `nonaliased`) to steer the output format yourself. They act much like the matching options.

[Subject index](INDEX.md) · [Previous](platform-android-ver.md) · [Continue](../plistlib/plistlib-load-to-plistlib-loads.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
