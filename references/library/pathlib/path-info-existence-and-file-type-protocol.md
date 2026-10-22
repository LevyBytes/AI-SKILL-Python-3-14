# pathlib.types.PathInfo: `exists()`, `is_dir()`, `is_file()`, `is_symlink()`

exists(***, *follow_symlinks=True*)

Hand back `True` when the path is an existing file or directory, or indeed any other kind of file; hand back `False` when the path is absent.

With *follow_symlinks* set to `False`, hand back `True` for symlinks without ever checking whether their targets exist.

 is_dir(***, *follow_symlinks=True*)

Hand back `True` when the path is a directory, or a symbolic link aimed at a directory; hand back `False` when the path is (or points to) any other kind of file, or when it's absent.

With *follow_symlinks* set to `False`, hand back `True` solely when the path is a directory (without chasing symlinks); hand back `False` when the path is any other kind of file, or when it's absent.

 is_file(***, *follow_symlinks=True*)

Hand back `True` when the path is a file, or a symbolic link aimed at a file; hand back `False` when the path is (or points to) a directory or some other non-file, or when it's absent.

With *follow_symlinks* set to `False`, hand back `True` solely when the path is a file (without chasing symlinks); hand back `False` when the path is a directory or some other non-file, or when it's absent.

 is_symlink()

Hand back `True` when the path is a symbolic link (broken or not); hand back `False` when the path is a directory or any kind of file, or when it's absent.

[Subject index](INDEX.md) · [Previous](pathlib-types-pathinfo-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: pathlib.types.PathInfo](pathlib-types-pathinfo-class.md) · [Owning module, declaration or section: Protocols](pathlib-types-pathinfo-class.md)
