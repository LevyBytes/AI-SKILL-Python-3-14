# What’s New In Python 3.5 / pathlib — os, pathlib

### pathlib

To verify whether a path refers to the same file as another path ? which may itself be a different [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) object or a string ? you can use the new [`Path.samefile()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.samefile) method:

```python
>>> import pathlib
>>> p1 = pathlib.Path('/etc/hosts')
>>> p2 = pathlib.Path('/etc/../etc/hosts')
>>> p1.samefile(p2)
True

```

(Contributed by Vajrasky Kok and Antoine Pitrou in [bpo-19775](https://bugs.python.org/issue?@action=redirect&bpo=19775).)

To line up with `mkdir -p` and [`os.makedirs()`](https://docs.python.org/3.14/library/os.html#os.makedirs) behavior, the [`Path.mkdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.mkdir) method now takes a new optional *exist_ok* argument. (Contributed by Berker Peksag in [bpo-21539](https://bugs.python.org/issue?@action=redirect&bpo=21539).)

For expanding `~` and `~user` prefixes there is a new [`Path.expanduser()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.expanduser) method. (Contributed by Serhiy Storchaka and Claudiu Popa in [bpo-19776](https://bugs.python.org/issue?@action=redirect&bpo=19776).)

To obtain a [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) instance that stands for the user's home directory, you can call the new [`Path.home()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.home) class method. (Contributed by Victor Salgado and Mayank Tripathi in [bpo-19777](https://bugs.python.org/issue?@action=redirect&bpo=19777).)

To make reading from and writing to files easier, there are new [`Path.write_text()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.write_text), [`Path.read_text()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.read_text), [`Path.write_bytes()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.write_bytes), [`Path.read_bytes()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.read_bytes) methods.

Running the snippet below builds, or overwrites, the existing file `~/spam42`:

```python
>>> import pathlib
>>> p = pathlib.Path('~/spam42')
>>> p.expanduser().write_text('ham')
3

```

(Contributed by Christopher Welborn in [bpo-20218](https://bugs.python.org/issue?@action=redirect&bpo=20218).)

### pickle

[Subject index](INDEX.md) · [Previous source section](os.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](pickle.md)
