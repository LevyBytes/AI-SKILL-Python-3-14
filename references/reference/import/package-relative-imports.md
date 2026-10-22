# 5.7. Package Relative Imports

### 5.7. Package Relative Imports

Leading dots mark relative imports. One leading dot stands for a relative import that begins at the current package. Two or more leading dots stand for a relative import reaching up to the parent(s) of the current package, climbing one level for each dot past the first. To illustrate, take the following package layout:

```python
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py

```

Within either `subpackage1/moduleX.py` or `subpackage1/__init__.py`, these count as valid relative imports:

```python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo

```

Absolute imports are free to take either the `import <>` form or the `from <> import <>` form, yet relative imports are restricted to the second one; the rationale is that:

```python
import XXX.YYY.ZZZ

```

is meant to make `XXX.YYY.ZZZ` available as a usable expression, whereas .moduleY does not constitute a valid expression.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](replacing-the-standard-import-system.md) · [Following source section](special-considerations-for-main.md)
