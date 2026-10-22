# Python 3.10.0 beta 1 / library / functions and types

[bpo-25478](https://bugs.python.org/issue?@action=redirect&bpo=25478): A *total()* method now exists on collections.Counter() for totaling the counts.

[bpo-43680](https://bugs.python.org/issue?@action=redirect&bpo=43680): io.OpenWrapper and _pyio.OpenWrapper are deprecated: reach for io.open and _pyio.open instead. Up through Python 3.9, because _pyio.open was not yet a static method, builtins.open had to be aimed at OpenWrapper so that, once placed on a class variable, it would not become a bound method. Note that _io.open counts as a built-in function while _pyio.open counts as a Python-level function. Beginning with Python 3.10, _pyio.open() has become a static method, and io.open() is what builtins.open() now refers to.

[bpo-43764](https://bugs.python.org/issue?@action=redirect&bpo=43764): Give the @dataclass decorator a match_args parameter so __match_args__ generation can be turned off.

[bpo-43789](https://bugs.python.org/issue?@action=redirect&bpo=43789): OpenSSL 3.0.0: Skip invoking the password callback function a second time once the first invocation has flagged an error condition.

[bpo-42269](https://bugs.python.org/issue?@action=redirect&bpo=42269): A `slots` parameter was added to the `dataclasses.dataclass` decorator so that `__slots__` is generated automatically for the class. Yurii Karabas provided this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
