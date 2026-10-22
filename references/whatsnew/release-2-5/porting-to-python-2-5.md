# What's New in Python 2.5 / Porting to Python 2.5 — csv, locale, pickle, xmlrpc.server

### Porting to Python 2.5

The items below recap earlier-mentioned changes that might force edits to your own code:

- Modules now default to ASCII as their encoding. A module that includes string literals containing 8-bit characters without an encoding declaration now raises a syntax error. Under Python 2.4 the same situation produced only a warning rather than an error.

- A generator’s `gi_frame` attribute used to always be a frame object. Owing to the [**PEP 342**](https://peps.python.org/pep-0342/) changes covered in the PEP 342: New Generator Features section, `gi_frame` can now hold `None`.

- A fresh warning, [`UnicodeWarning`](https://docs.python.org/3.14/library/exceptions.html#UnicodeWarning), now fires whenever you try comparing a Unicode string against an 8-bit string that the default ASCII encoding cannot decode. Formerly that kind of comparison raised a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) exception instead.

- Library: the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module enforces tighter rules on quoted fields that span several lines. When your data embeds newlines inside fields, you should break the input into lines in a way that retains those newline characters.

- Library: the [`format()`](https://docs.python.org/3.14/library/functions.html#format) function in the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module formerly tolerated any string provided no more than a single %char specifier was present. Beginning with Python 2.5, the argument has to consist of exactly one %char specifier and nothing around it.

- Library: neither the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module nor `cPickle` will any longer accept `None` as the result of a [`__reduce__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce__) method; that method is now required to hand back a tuple of arguments. Both modules have likewise dropped support for the obsolete *bin* keyword parameter.

- Library: the [`SimpleXMLRPCServer`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) and `DocXMLRPCServer` classes have gained an `rpc_paths` attribute that restricts XML-RPC calls to a small set of URL paths; by default only `'/'` and `'/RPC2'` are permitted. Assigning `None` or an empty tuple to `rpc_paths` switches this path restriction off.

- C API: To enable handling larger amounts of data on 64-bit hardware, numerous functions have switched from int to [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t). Extension code may have to adopt the same switch so it avoids warnings and works on 64-bit machines. The earlier PEP 353: Using ssize_t as the index type section explains this change in detail.

- C API: Because of the obmalloc rework you have to avoid intermixing the `PyMem_*` and `PyObject_*` function families. Whatever you allocate with one family’s `*_Malloc` has to be released through that same family’s `*_Free` function.

[Subject index](INDEX.md) · [Previous source section](port-specific-changes.md) · [Next source section](acknowledgements.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
