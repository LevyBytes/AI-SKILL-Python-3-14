# Python 3.11.0 alpha 1 / library / inspect

[bpo-40897](https://bugs.python.org/issue?@action=redirect&bpo=40897): [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) now favors the current class constructor first. Weipeng Hong wrote the patch.

[bpo-44648](https://bugs.python.org/issue?@action=redirect&bpo=44648): Corrected the wrong error raised by [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) while inspecting a class within an interactive session. Rather than a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), the call should yield an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) carrying a fitting message.

[bpo-20684](https://bugs.python.org/issue?@action=redirect&bpo=20684): The unused `_signature_get_bound_param` function has been dropped from [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect); Anthony Sottile handled this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
