# tarfile — Writing examples

### Writing examples

Building an uncompressed tar archive out of a list of filenames:

```python
import tarfile
tar = tarfile.open("sample.tar", "w")
for name in ["foo", "bar", "quux"]:
    tar.add(name)
tar.close()

```

That same example written with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)

```

Creating an archive and writing it to stdout by passing [`sys.stdout.buffer`](https://docs.python.org/3.14/library/sys.html#sys.stdout) as the *fileobj* parameter in `TarFile.add()`:

```python
import sys
import tarfile
with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)

```

Creating an archive while clearing the user information by way of the *filter* parameter in `TarFile.add()`:

```python
import tarfile
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo
tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)
tar.close()

```

[Subject index](INDEX.md) · [Previous](reading-examples.md) · [Continue](supported-tar-formats.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
