# 6.4.2. Intra-package References

### 6.4.2. Intra-package References

Once a package is laid out with nested subpackages — the way `sound` is arranged in this walkthrough — absolute imports give you a route to reach submodules that sit beneath sibling packages. Suppose, say, that `sound.filters.vocoder` has to pull in the `echo` module residing within `sound.effects`; the statement `from sound.effects import echo` does the job.

Relative imports are another option open to you, expressed through the `from module import name` style of statement. Here, dots placed at the front signal which current and enclosing packages take part in the relative reference. Working from inside the `surround` module, for instance, you might write:

```python
from . import echo
from .. import formats
from ..filters import equalizer

```

Bear in mind that what anchors a relative import is the package name attached to whichever module is doing the importing. Because the main module carries no package of its own, any module you plan to run as the entry point of a Python program is obliged to stick with absolute imports.

[Subject index](INDEX.md) · [Previous source section](importing-from-a-package.md) · [Following source section](packages-in-multiple-directories.md)
