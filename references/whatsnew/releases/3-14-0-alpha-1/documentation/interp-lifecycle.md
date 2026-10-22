# Python 3.14.0 alpha 1 / documentation / interp lifecycle

[bpo-34008](https://bugs.python.org/issue?@action=redirect&bpo=34008): The [`Py_Main()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Main) documentation is relocated out of the “Very High Level API” section and into the “Initialization and Finalization” section.

The text now spells out that `Py_Main` is generally expected to be called in place of `Py_Initialize` rather than following it (because `Py_Main` issues its own `Py_Initialize` call). It also records that calling both is supported, though which settings end up applied correctly varies by version.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
