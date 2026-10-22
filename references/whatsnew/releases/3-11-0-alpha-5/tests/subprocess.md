# Python 3.11.0 alpha 5 / tests / subprocess

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): Add a `test.support.requires_subprocess()` decorator for flagging tests that need a working [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module or `os.spawn*`. Processes are unsupported on the wasm32-emscripten platform.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
