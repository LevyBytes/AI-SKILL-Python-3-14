# Python 3.8.0 alpha 1 / core and builtins / modules

[bpo-34485](https://bugs.python.org/issue?@action=redirect&bpo=34485): To set up the encoding for standard streams such as sys.stdout, Python now obtains the locale encoding from C code. Furthermore, that encoding is now resolved to its Python codec name, giving a normalized encoding name and confirming the codec actually loads. This change keeps the _bootlocale and _locale modules from being imported at startup by default.

[bpo-33331](https://bugs.python.org/issue?@action=redirect&bpo=33331): At interpreter shutdown, the modules imported most recently are now cleared earliest.

[bpo-35214](https://bugs.python.org/issue?@action=redirect&bpo=35214): Annotations were applied to the interpreter and the extension modules so they behave correctly beneath clang's Memory Sanitizer. To make such test builds easier, the configure step gained a `--with-memory-sanitizer` flag.

[bpo-28401](https://bugs.python.org/issue?@action=redirect&bpo=28401): Debug builds will from now on stop trying to import extension modules built for the ABI since they were never compatible to start with. Patch by Stefano Rivera.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
