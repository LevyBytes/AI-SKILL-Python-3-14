# subinterpreters C API: `Py_NewInterpreterFromConfig()`, `Py_NewInterpreter()`, `Py_EndInterpreter()`

[PyStatus](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus) Py_NewInterpreterFromConfig([PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) **tstate_p, const PyInterpreterConfig *config)

Bring a fresh sub-interpreter into existence. What you get is a setting that is (nearly) wholly distinct for running Python code. Specifically, this fresh interpreter holds its own independent copies of every imported module, the core ones [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins), [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) and [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) included. Likewise distinct are the loaded-module table (`sys.modules`) plus the module search path (`sys.path`). No `sys.argv` variable exists in this fresh setting. It supplies brand-new standard-I/O stream file objects `sys.stdin`, `sys.stdout` and `sys.stderr` (these nonetheless point at the very same underlying file descriptors).

Whatever *config* you hand in governs the settings the interpreter starts up with.

Once it succeeds, *tstate_p* gets pointed at the very first [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) produced within the fresh sub-interpreter. That thread state is [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). Be aware that no genuine thread comes into being; consult the thread-state discussion further down. Should building the fresh interpreter fail, *tstate_p* lands at `NULL`; nor is any exception recorded, given that exception state resides in the attached thread state, which may be absent.

In keeping with every other Python/C API function, an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) has to exist ahead of invoking this function, though it could end up detached once it returns. When it succeeds, the thread state given back will be attached. Where the sub-interpreter is built with a [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) of its own, the calling interpreter's attached thread state gets detached. By the time the function returns, the fresh interpreter's [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) sits attached to the present thread while the prior interpreter's attached thread state stays detached.

Added in version 3.12.

You get the best results from sub-interpreters by keeping them isolated from one another and clamping down on particular capabilities:

```c
PyInterpreterConfig config = {
    .use_main_obmalloc = 0,
    .allow_fork = 0,
    .allow_exec = 0,
    .allow_threads = 1,
    .allow_daemon_threads = 0,
    .check_multi_interp_extensions = 1,
    .gil = PyInterpreterConfig_OWN_GIL,
};
PyThreadState *tstate = NULL;
PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config);
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}

```

Bear in mind the config sees only momentary use and stays unmodified. As startup proceeds, the config's values get translated into assorted `PyInterpreterState` values. The `PyInterpreterState` may keep a read-only copy of the config internally.

Here is the way extension modules end up shared across (sub-)interpreters:

- Where modules lean on multi-phase initialization — say [`PyModule_FromDefAndSpec()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_FromDefAndSpec) — every interpreter gets its own module object built and set up. What these module objects hold in common is limited to C-level static and global variables.

- Where modules rely on legacy [single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization) — for instance [`PyModule_Create()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_Create) — the very first import of a given extension runs the usual initialization and tucks away a shallow copy of that module's dictionary. Later, when some other (sub-)interpreter imports that same extension, a fresh module is set up and loaded with whatever this copy holds; the extension's `init` function goes uncalled. As a result the objects within the module's dictionary wind up shared across (sub-)interpreters, a state of affairs that can produce undesired effects (consult Bugs and caveats further down).

Be aware this diverges from what occurs when an extension is imported once the interpreter has been wholly reinitialized via [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) followed by [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize); under that scenario the extension's `initmodule` function *does* run a second time. Just as with multi-phase initialization, the upshot is that these modules share nothing beyond C-level static and global variables.

 [PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *Py_NewInterpreter(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Bring a fresh sub-interpreter into existence. At bottom this merely wraps `Py_NewInterpreterFromConfig()` using a config that keeps the prior behavior intact. You end up with a non-isolated sub-interpreter that shares the main interpreter's GIL, permits fork/exec, permits daemon threads, and permits single-phase-init modules.

 void Py_EndInterpreter([PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Tear down whatever (sub-)interpreter the supplied [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) stands for. That thread state has to be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). After the call comes back, no attached thread state remains. Every thread state tied to this interpreter gets torn down.

Any sub-interpreters not already explicitly torn down by that moment will be torn down by [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](multiple-interpreters-in-a-python-process.md) · [Owning structure and shared ABI conditions](pyinterpreterconfig-to-pyinterpreterconfig-own-gil.md) · [Following source contract](py-newinterpreterfromconfig.md)
