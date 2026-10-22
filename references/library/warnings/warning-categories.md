# warnings — Warning Categories

### Warning Categories

Several built-in exceptions stand for warning categories. Grouping warnings this way makes it possible to filter whole sets of them at once.

Although they are strictly speaking [built-in exceptions](https://docs.python.org/3.14/library/exceptions.html#warning-categories-as-exceptions), they appear here in the docs because, conceptually, they are part of the warnings mechanism.

You can add your own warning categories in user code by deriving from any of the standard ones. Every warning category has to descend from the [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) class.

These are the warning category classes defined at present:

| Class | Description |
| --- | --- |
| `Warning` | The root from which every warning category class descends; itself a subclass of `Exception`. |
| `UserWarning` | The category `warn()` uses by default. |
| `DeprecationWarning` | Base category covering deprecated features whose warnings target fellow Python developers (ignored by default, save when raised by code in `__main__`). |
| `SyntaxWarning` | Base category covering questionable syntactic constructs (usually raised while compiling Python source, so runtime filters may be unable to suppress them) |
| `RuntimeWarning` | Base category covering questionable behaviour at runtime. |
| `FutureWarning` | Base category covering deprecated features whose warnings target the end users of applications built in Python. |
| `PendingDeprecationWarning` | Base category covering features slated for deprecation down the line (ignored by default). |
| `ImportWarning` | Base category covering warnings raised while a module is being imported (ignored by default). |
| `UnicodeWarning` | Base category covering warnings tied to Unicode. |
| `BytesWarning` | Base category covering warnings tied to `bytes` and `bytearray`. |
| `ResourceWarning` | Base category covering warnings tied to resource usage (ignored by default). |

Changed in version 3.7: Earlier, the split between [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) and [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) turned on whether a feature was going away completely or merely altering how it behaved. The distinction now rests on who the message is aimed at and on how the default warnings filters deal with each one.

[Subject index](INDEX.md) · [Previous](warnings-warning-control.md) · [Continue](the-warnings-filter.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
