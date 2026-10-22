# modulefinder — Example usage of `ModuleFinder`

### Example usage of `ModuleFinder`

The script that is going to get analyzed later on (bacon.py):

```python
import re, itertools

try:
    import baconhameggs
except ImportError:
    pass

try:
    import guido.python.ham
except ImportError:
    pass

```

The script that will output the report of bacon.py:

```python
from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('bacon.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('Modules not imported:')
print('\n'.join(finder.badmodules.keys()))

```

Sample output (may vary depending on the architecture):

```python
Loaded modules:
_types:
copyreg:  _inverted_registry,_slotnames,__all__
re._compiler:  isstring,_sre,_optimize_unicode
_sre:
re._constants:  REPEAT_ONE,makedict,AT_END_LINE
sys:
re:  __module__,finditer,_expand
itertools:
__main__:  re,itertools,baconhameggs
re._parser:  _PATTERNENDERS,SRE_FLAG_UNICODE
array:
types:  __module__,IntType,TypeType
---------------------------------------------------
Modules not imported:
guido.python.ham
baconhameggs

```

[Subject index](INDEX.md) · [Previous](module-finder-analysis-and-script-execution.md) · [Continue](../modules/importing-modules.md) · [Owning module, declaration or section: modulefinder](modulefinder-addpackagepath-to-modulefinder-replacepackage.md)
