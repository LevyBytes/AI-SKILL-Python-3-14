# pathlib - Comparison to the `glob` module

### Comparison to the [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module

The patterns taken and the results produced by `Path.glob()` and `Path.rglob()` part ways in a few small respects from those of the [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module:

1.

Within pathlib, files whose names start with a dot get no special treatment. That mirrors handing `include_hidden=True` to [`glob.glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob).

2.

Within pathlib, “`**`” pattern components always recurse. That mirrors handing `recursive=True` to [`glob.glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob).

3.

Within pathlib, “`**`” pattern components by default leave symlinks unfollowed. [`glob.glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob) has nothing matching this behaviour, though handing `recurse_symlinks=True` to `Path.glob()` gives you the compatible behaviour.

4.

As with every `PurePath` and `Path` object, whatever `Path.glob()` and `Path.rglob()` return carries no trailing slashes.

5.

Whatever pathlib's `path.glob()` and `path.rglob()` return carries the *path* as a leading prefix, which sets it apart from the output of `glob.glob(root_dir=path)`.

6.

Whatever pathlib's `path.glob()` and `path.rglob()` return can take in *path* itself — say when globbing “`**`” — while `glob.glob(root_dir=path)`'s output never holds an empty string standing for *path*.

[Subject index](INDEX.md) · [Previous](pattern-language.md) · [Continue](comparison-to-the-os-and-os-path-modules.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
