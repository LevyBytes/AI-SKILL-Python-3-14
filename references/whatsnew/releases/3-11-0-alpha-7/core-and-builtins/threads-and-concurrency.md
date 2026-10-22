# Python 3.11.0 alpha 7 / core and builtins / threads and concurrency

[bpo-47176](https://bugs.python.org/issue?@action=redirect&bpo=47176): Platform constraints mean Emscripten builds cannot process signals through the ordinary mechanism. Signal handling is now available in Python regardless. To turn it on, point Module.Py_EmscriptenSignalBuffer at a one-byte SharedArrayBuffer and assign Py_EMSCRIPTEN_SIGNAL_HANDLING the value 1. Storing a number inside the SharedArrayBuffer raises the matching signal into the Python thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
