# pathlib - Corresponding tools

### Corresponding tools

The table that follows pairs assorted [`os`](https://docs.python.org/3.14/library/os.html#module-os) functions with their matching `PurePath`/`Path` counterpart.

| `os` and `os.path` | `pathlib` |
| --- | --- |
| `os.path.dirname()` | `PurePath.parent` |
| `os.path.basename()` | `PurePath.name` |
| `os.path.splitext()` | `PurePath.stem`, `PurePath.suffix` |
| `os.path.join()` | `PurePath.joinpath()` |
| `os.path.isabs()` | `PurePath.is_absolute()` |
| `os.path.relpath()` | `PurePath.relative_to()` [1] |
| `os.path.expanduser()` | `Path.expanduser()` [2] |
| `os.path.realpath()` | `Path.resolve()` |
| `os.path.abspath()` | `Path.absolute()` [3] |
| `os.path.exists()` | `Path.exists()` |
| `os.path.isfile()` | `Path.is_file()` |
| `os.path.isdir()` | `Path.is_dir()` |
| `os.path.islink()` | `Path.is_symlink()` |
| `os.path.isjunction()` | `Path.is_junction()` |
| `os.path.ismount()` | `Path.is_mount()` |
| `os.path.samefile()` | `Path.samefile()` |
| `os.getcwd()` | `Path.cwd()` |
| `os.stat()` | `Path.stat()` |
| `os.lstat()` | `Path.lstat()` |
| `os.listdir()` | `Path.iterdir()` |
| `os.walk()` | `Path.walk()` [4] |
| `os.mkdir()`, `os.makedirs()` | `Path.mkdir()` |
| `os.link()` | `Path.hardlink_to()` |
| `os.symlink()` | `Path.symlink_to()` |
| `os.readlink()` | `Path.readlink()` |
| `os.rename()` | `Path.rename()` |
| `os.replace()` | `Path.replace()` |
| `os.remove()`, `os.unlink()` | `Path.unlink()` |
| `os.rmdir()` | `Path.rmdir()` |
| `os.chmod()` | `Path.chmod()` |
| `os.lchmod()` | `Path.lchmod()` |

Footnotes

[Subject index](INDEX.md) · [Previous](comparison-to-the-os-and-os-path-modules.md) · [Continue](pathlib-types-pathinfo-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
