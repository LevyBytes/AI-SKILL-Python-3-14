# Python 3.6.3 release candidate 1 / core and builtins / functions and types

[bpo-31271](https://bugs.python.org/issue?@action=redirect&bpo=31271): Repair an assertion failure within the `write()` method belonging to `io.TextIOWrapper` whenever the encoder fails to return a bytes object. Oren Milman wrote the patch.

[bpo-31243](https://bugs.python.org/issue?@action=redirect&bpo=31243): Repair a crash across several methods of `io.TextIOWrapper` whenever the decoder's state is invalid. Oren Milman wrote the patch.

[bpo-31095](https://bugs.python.org/issue?@action=redirect&bpo=31095): Repair a possible crash while GC runs, brought on by a `tp_dealloc` that omits the `PyObject_GC_UnTrack()` call.

[bpo-31071](https://bugs.python.org/issue?@action=redirect&bpo=31071): Stop the original TypeError from being masked in a call using * unpacking whenever other arguments are passed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
