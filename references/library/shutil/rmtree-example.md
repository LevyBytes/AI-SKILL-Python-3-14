# shutil - rmtree example

### rmtree example

Here’s how to delete a directory tree under Windows when a few of its files carry the read-only bit. The onexc callback is enlisted to clear that readonly bit and have another go at removing the file. Should it fail again, that failure is allowed to propagate.

```python
import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(directory, onexc=remove_readonly)

```

[Subject index](INDEX.md) · [Previous](copytree-example.md) · [Continue](shutil-make-archive-to-shutil-get-archive-formats.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
