# What's New In Python 3.10 / Porting to Python 3.10 / Changes in the C API

### Changes in the C API

- Because the project moved to the new PEG parser, the C API functions `PyParser_SimpleParseStringFlags`, `PyParser_SimpleParseStringFlagsFilename`, `PyParser_SimpleParseFileFlags`, `PyNode_Compile`, plus `struct _node` (the type they relied on), have been removed.

The recommended approach now is to compile source straight into a code object — for instance with [`Py_CompileString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.Py_CompileString). You can then run that code object using something like [`PyEval_EvalCode()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyEval_EvalCode).

In detail:

  - Where you once called `PyParser_SimpleParseStringFlags` and then `PyNode_Compile`, a single call to [`Py_CompileString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.Py_CompileString) now does the job.

  - `PyParser_SimpleParseFileFlags` has no straight substitute. To compile from a `FILE *` argument, read the file yourself in C and feed the resulting buffer to [`Py_CompileString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.Py_CompileString).

  -

When you have only a `char *` filename and want to compile that file, you must open it yourself, read its contents, then compile what you read. A typical route relies on the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module together with [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule), [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod), [`PyBytes_AsString()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_AsString) and [`Py_CompileString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.Py_CompileString), roughly as the snippet below shows. (For brevity, declarations plus error checks are left out.)

```python
io_module = Import_ImportModule("io");
fileobject = PyObject_CallMethod(io_module, "open", "ss", filename, "rb");
source_bytes_object = PyObject_CallMethod(fileobject, "read", "");
result = PyObject_CallMethod(fileobject, "close", "");
source_buf = PyBytes_AsString(source_bytes_object);
code = Py_CompileString(source_buf, filename, Py_file_input);

```

  - When dealing with `FrameObject` objects, the [`f_lasti`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lasti) member now carries a wordcode offset rather than a plain offset into the bytecode string. As a consequence, you must double this value (multiply by 2) before handing it to APIs expecting a byte offset (for instance [`PyCode_Addr2Line()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_Addr2Line)). Keep in mind too that the `f_lasti` member belonging to `FrameObject` objects is not treated as stable: prefer [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber) in its place.

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-10.md) · [Next source section](bytecode-migration-changes.md)
