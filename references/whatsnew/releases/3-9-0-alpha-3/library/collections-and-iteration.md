# Python 3.9.0 alpha 3 / library / collections and iteration

[bpo-39152](https://bugs.python.org/issue?@action=redirect&bpo=39152): ttk.Scale.configure([name]) was fixed so it returns the configuration tuple for a given name or for all options. Giovanni Lombardo contributed part of the patch.

[bpo-39142](https://bugs.python.org/issue?@action=redirect&bpo=39142): logging.config.dictConfig was altered so it no longer turns named tuple instances into ConvertingTuple. The reasoning is that named tuples are too specialised to be handled as plain tuples; anyone whose named tuples need ConvertingTuple behavior must add it themselves within their own named tuple class.

[bpo-21600](https://bugs.python.org/issue?@action=redirect&bpo=21600): `mock.patch.stopall()` was fixed to halt active patches that had been set up via `mock.patch.dict()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
