# __main__ — `__main__.py` in Python Packages

### `__main__.py` in Python Packages

If Python packages are unfamiliar territory, turn to the tutorial's [Packages](https://docs.python.org/3.14/tutorial/modules.html#tut-packages) section. The `__main__.py` file most often exists to give a package its command-line interface. Picture this made-up package, “bandclass”:

```text
bandclass
  ├── __init__.py
  ├── __main__.py
  └── student.py

```

Running the package itself straight from the command line with the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) flag triggers `__main__.py`. As an illustration:

```shell
$ python -m bandclass

```

That command sets `__main__.py` running. Just how you put this mechanism to work hinges on the kind of package you're building, but for this made-up example it could be reasonable to let the teacher look up students:

```python
# bandclass/__main__.py

import sys
from .student import search_students

student_name = sys.argv[1] if len(sys.argv) >= 2 else ''
print(f'Found student: {search_students(student_name)}')

```

Observe that `from .student import search_students` illustrates a relative import. You can lean on this import form when pointing at modules that live inside a package. For the full story, see [Intra-package References](https://docs.python.org/3.14/tutorial/modules.html#intra-package-references) within the tutorial's [Modules](https://docs.python.org/3.14/tutorial/modules.html#tut-modules) section.

[Subject index](INDEX.md) · [Previous](packaging-considerations.md) · [Continue](idiomatic-usage.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md)
