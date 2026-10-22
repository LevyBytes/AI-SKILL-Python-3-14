# shutil — copytree example

### copytree example

An example built around the `ignore_patterns()` helper:

```python
from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

```

This copies everything apart from `.pyc` files and any file or directory whose name begins with `tmp`.

Another example that uses the *ignore* argument to add a logging call:

```python
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)

```

[Subject index](INDEX.md) · [Previous](platform-dependent-efficient-copy-operations.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Continue](rmtree-example.md)
