# tarfile — Reading examples

### Examples

### Reading examples

Pulling a whole tar archive out into the current working directory:

```python
import tarfile
tar = tarfile.open("sample.tar.gz")
tar.extractall(filter='data')
tar.close()

```

Pulling out only part of a tar archive via `TarFile.extractall()`, supplying a generator function rather than a list:

```python
import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=py_files(tar))
tar.close()

```

Reading a gzip-compressed tar archive and printing out some member details:

```python
import tarfile
tar = tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()

```

[Subject index](INDEX.md) · [Continue](writing-examples.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
