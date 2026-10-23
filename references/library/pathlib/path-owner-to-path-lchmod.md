# pathlib - Permissions and ownership

### Permissions and ownership

 Path.owner(***, *follow_symlinks=True*)

Hand back the name of the user who owns the file. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the file's user identifier (UID) can't be located in the system database.

By default this method tracks symlinks; to learn the owner of the symlink instead, tack on the argument `follow_symlinks=False`.

Changed in version 3.13: `UnsupportedOperation` is raised whenever the [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd) module can't be used. Older releases raised [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) there.

Changed in version 3.13: The *follow_symlinks* parameter was added.

 Path.group(***, *follow_symlinks=True*)

Hand back the name of the group that owns the file. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the file's group identifier (GID) can't be located in the system database.

By default this method tracks symlinks; to learn the group of the symlink instead, tack on the argument `follow_symlinks=False`.

Changed in version 3.13: `UnsupportedOperation` is raised whenever the [`grp`](https://docs.python.org/3.14/library/grp.html#module-grp) module can't be used. Older releases raised [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) there.

Changed in version 3.13: The *follow_symlinks* parameter was added.

 Path.chmod(*mode*, ***, *follow_symlinks=True*)

Change the file mode and permissions, like [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod).

By default this method tracks symlinks. A handful of Unix flavours let you change permissions on the symlink itself; on those platforms you can either tack on the argument `follow_symlinks=False` or turn to `lchmod()`.

```python
>>> p = Path('setup.py')
>>> p.stat().st_mode
33277
>>> p.chmod(0o444)
>>> p.stat().st_mode
33060

```

Changed in version 3.10: The *follow_symlinks* parameter was added.

 Path.lchmod(*mode*)

Behaves like `Path.chmod()`, except that when the path refers to a symbolic link, it's the symbolic link's own mode that changes rather than the mode of its target.

[Subject index](INDEX.md) · [Previous](path-copy-to-path-rmdir.md) · [Continue](pattern-language.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
