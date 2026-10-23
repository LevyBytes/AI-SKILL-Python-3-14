# What’s New In Python 3.5 / unittest.mock - unittest.mock

### unittest.mock

These enhancements have come to the [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) class:

- An *unsafe* parameter has been added to the class constructor; it makes mock objects throw [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) for any attribute name that begins with `"assert"`. Kushal Das contributed this (see [bpo-21238](https://bugs.python.org/issue?@action=redirect&bpo=21238)).

- To verify that a mock object went uncalled, there is a new [`Mock.assert_not_called()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_not_called) method. Kushal Das landed this (see [bpo-21262](https://bugs.python.org/issue?@action=redirect&bpo=21262)).

The [`__truediv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__truediv__), [`__divmod__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__divmod__) and [`__matmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__matmul__) operators are now supported by the [`MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) class. Johannes Baiter added support (see [bpo-20968](https://bugs.python.org/issue?@action=redirect&bpo=20968)), and Håkan Lövdahl added more (see [bpo-23581](https://bugs.python.org/issue?@action=redirect&bpo=23581) and [bpo-23568](https://bugs.python.org/issue?@action=redirect&bpo=23568)).

Passing `create=True` explicitly to the [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) function is no longer required when you patch builtin names. (Contributed by Kushal Das in [bpo-17660](https://bugs.python.org/issue?@action=redirect&bpo=17660).)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](urllib.md)
