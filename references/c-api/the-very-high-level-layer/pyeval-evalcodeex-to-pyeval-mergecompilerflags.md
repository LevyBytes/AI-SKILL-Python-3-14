# the very high level layer C API: `PyEval_EvalCodeEx()`, `PyEval_EvalFrame()`, `PyEval_EvalFrameEx()`, `PyEval_MergeCompilerFlags()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_EvalCodeEx([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *args, int argcount, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *kws, int kwcount, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *defs, int defcount, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwdefs, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *closure)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Evaluates a code object that has already been compiled, given a specific environment in which to evaluate it. The pieces of that environment are: a dictionary holding the global variables; a mapping object for the locals; arrays that carry the positional arguments, the keywords, and the defaults; for [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter) arguments, a dictionary supplying their default values; plus a tuple of cells forming the closure.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_EvalFrame([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *f)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Evaluates an execution frame. This is a simplified interface to `PyEval_EvalFrameEx()`, kept for backward compatibility.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_EvalFrameEx([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *f, int throwflag)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is Python's core evaluation routine, presented without any embellishment. The code object attached to execution frame *f* runs, with bytecode being interpreted and calls being made as required. The extra *throwflag* parameter can usually be left alone - when it is true, an exception is thrown right away; this serves the [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) methods on generator objects.

Changed in version 3.4: A debug assertion was added to this function so that an active exception cannot be quietly thrown away.

 int PyEval_MergeCompilerFlags(PyCompilerFlags *cf)

This function alters the flags on the current evaluation frame and gives back true when it succeeds, false when it fails.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyrun-anyfile-to-pyrun-interactiveloopflags.md) · [Previous source contract](pyrun-string-to-pyeval-evalcode.md) · [Following source contract](pycompilerflags-to-pycf-type-comments.md)
