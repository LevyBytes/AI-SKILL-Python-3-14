# What’s New In Python 3.5 / importlib — importlib, types

### importlib

For applications that care about startup time, the [`util.LazyLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.util.LazyLoader) class makes lazy module loading possible. (Contributed by Brett Cannon in [bpo-17621](https://bugs.python.org/issue?@action=redirect&bpo=17621).)

A static method is what the [`abc.InspectLoader.source_to_code()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader.source_to_code) method has become. Setting up a module object from code compiled out of a string is now simpler through `exec(code, module.__dict__)`. (Contributed by Brett Cannon in [bpo-21156](https://bugs.python.org/issue?@action=redirect&bpo=21156).)

For building a new module, the recommended approach is now the new [`util.module_from_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.module_from_spec) function. Rather than building a [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) instance straight away, this new function configures the assorted import-controlled attributes from the spec object it receives. (Contributed by Brett Cannon in [bpo-20383](https://bugs.python.org/issue?@action=redirect&bpo=20383).)

[Subject index](INDEX.md) · [Previous source section](imghdr.md) · [Next source section](inspect.md) · [Release/subject declaration](summary-release-highlights.md)
