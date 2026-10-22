# Python 3.9.0 alpha 6 / library / inspect

[bpo-40257](https://bugs.python.org/issue?@action=redirect&bpo=40257): [`inspect.getdoc()`](https://docs.python.org/3.14/library/inspect.html#inspect.getdoc) at this point declines to return a docstring inherited from the object's type, or from a parent class when it is a class, unless that docstring is defined on the object itself. Inside [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) the documentation string at this point appears not merely for a class, function, method and so on, but for any object owning its own `__doc__` attribute.

[bpo-35113](https://bugs.python.org/issue?@action=redirect&bpo=35113): [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) now hands back the right source for an inner class that shares its name with a module-level class. Any decorators come along as part of the class source too. Karthikeyan Singaravelan wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
