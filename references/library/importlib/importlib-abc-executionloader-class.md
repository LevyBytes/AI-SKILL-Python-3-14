# importlib: `importlib.abc.ExecutionLoader`

*class *importlib.abc.ExecutionLoader

An abstract base class that derives from `InspectLoader` and, once implemented, makes it possible to run a module as a script. This ABC stands for an optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol.

 *abstractmethod *get_filename(*fullname*)

>

An abstract method whose job is to yield the [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) value for the named module. Where no path can be had, [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised.

Where the source code is on hand, the method ought to give back the path to the source file, no matter whether bytecode was what actually loaded the module.

Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

[Subject index](INDEX.md) · [Previous](abstract-inspect-loader.md) · [Continue](abstract-file-loader.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
