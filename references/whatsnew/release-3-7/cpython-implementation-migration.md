# What's New In Python 3.7 / Porting to Python 3.7 / Changes in the C API / Other CPython implementation changes

### Other CPython implementation changes

Anticipating possible later revisions to the public CPython runtime initialization API (consult [**PEP 432**](https://peps.python.org/pep-0432/) for an early, though by now somewhat stale, draft), the internal startup and configuration management logic of CPython was substantially reworked. Although these updates are meant to stay completely invisible to embedding applications as well as to users of the ordinary CPython CLI, they get noted here because the refactoring reorders various internal operations occurring while the interpreter starts, and may thereby expose formerly hidden defects, whether in embedding applications or within CPython itself. Nick Coghlan and Eric Snow kicked this off as part of [bpo-22257](https://bugs.python.org/issue?@action=redirect&bpo=22257), with later updates from Nick, Eric, and Victor Stinner across a number of further issues. A few known particulars touched:

- `PySys_AddWarnOptionUnicode()` cannot presently be used by embedding applications, since it demands constructing a Unicode object before `Py_Initialize` runs. Turn to `PySys_AddWarnOption()` in its place.

- warnings filters that an embedding application adds with `PySys_AddWarnOption()` should at present more reliably win out over the interpreter's own default filters

Because of revisions to how the default warnings filters get configured, raising [`Py_BytesWarningFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag) above one is no longer enough on its own to both emit [`BytesWarning`](https://docs.python.org/3.14/library/exceptions.html#BytesWarning) messages and turn them into exceptions. Rather, the flag has to be set (so that the warnings are emitted at all), plus an explicit `error::BytesWarning` warnings filter has to be added to convert them into exceptions.

Because of a shift in how the compiler treats docstrings, the implicit `return None` inside a function body made up solely of a docstring is at present recorded as happening on the docstring's own line rather than on the function's header line.

The active exception state was relocated off the frame object and onto the co-routine. That streamlined the interpreter and cleared up a couple of obscure bugs stemming from having to swap exception state on entering or leaving a generator. Mark Shannon contributed this through [bpo-25612](https://bugs.python.org/issue?@action=redirect&bpo=25612).

[Subject index](INDEX.md) · [Previous source section](windows-c-api-migration.md) · [Next source section](notable-changes-in-python-3-7-1.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-7.md) · [Release/subject declaration](porting-to-python-3-7-changes-in-the-c-api.md)
