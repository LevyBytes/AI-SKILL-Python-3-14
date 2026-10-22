# Warnings

### Warnings

The exceptions below serve as warning categories; consult the [Warning Categories](https://docs.python.org/3.14/library/warnings.html#warning-categories) documentation for fuller detail.

 *exception *Warning

The root class for the warning categories.

 *exception *UserWarning

The root class for warnings that user code produces.

 *exception *DeprecationWarning

The root class for warnings about deprecated features in cases where the audience for those warnings is fellow Python developers.

The default warning filters ignore this, save within the `__main__` module ([**PEP 565**](https://peps.python.org/pep-0565/)). Turning on the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) surfaces this warning.

[**PEP 387**](https://peps.python.org/pep-0387/) sets out the deprecation policy.

 *exception *PendingDeprecationWarning

The root class for warnings about features that are obsolete and slated for deprecation down the line, yet stand as not deprecated for now.

You will seldom see this class, since flagging a warning about a deprecation that might be coming is unusual, and `DeprecationWarning` is the choice for deprecations already in force.

The default warning filters ignore this. Turning on the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) surfaces this warning.

[**PEP 387**](https://peps.python.org/pep-0387/) sets out the deprecation policy.

 *exception *SyntaxWarning

The root class for warnings about questionable syntax.

This warning generally fires while Python source code is being compiled, and usually does not surface when you run code that is already compiled.

 *exception *RuntimeWarning

The root class for warnings about questionable runtime behavior.

 *exception *FutureWarning

The root class for warnings about deprecated features in cases where the audience for those warnings is end users of applications written in Python.

 *exception *ImportWarning

The root class for warnings about likely errors in module imports.

The default warning filters ignore this. Turning on the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) surfaces this warning.

 *exception *UnicodeWarning

The root class for warnings to do with Unicode.

 *exception *EncodingWarning

The root class for warnings to do with encodings.

For details, see [Opt-in EncodingWarning](https://docs.python.org/3.14/library/io.html#io-encoding-warning).

Added in version 3.10.

 *exception *BytesWarning

The root class for warnings to do with [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

 *exception *ResourceWarning

The root class for warnings to do with resource usage.

The default warning filters ignore this. Turning on the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) surfaces this warning.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](blockingioerror-to-timeouterror.md) · [Continue](exceptiongroup-to-split.md)
