# subinterpreters C API: `PyInterpreterConfig`, `PyInterpreterConfig_DEFAULT_GIL`, `PyInterpreterConfig_SHARED_GIL`, `PyInterpreterConfig_OWN_GIL`

type PyInterpreterConfig

A structure holding the bulk of the parameters for configuring a sub-interpreter. The runtime reads its values solely within `Py_NewInterpreterFromConfig()` and leaves them untouched otherwise.

Added in version 3.12.

Structure fields:

 int use_main_obmalloc

A value of `0` here means the sub-interpreter keeps its own “object” allocator state. Any other value makes it share the main interpreter’s instead.

Where this holds `0`, `check_multi_interp_extensions` is required to be `1` (non-zero). Where it holds `1`, `gil` may not be set to `PyInterpreterConfig_OWN_GIL`.

 int allow_fork

When this equals `0`, the runtime declines to permit forking the process from any thread in which the sub-interpreter happens to be active. Any other value leaves fork unconstrained.

Keep in mind that the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module continues to function even with fork forbidden.

 int allow_exec

When this equals `0`, the runtime declines to permit swapping out the current process by way of exec (for instance [`os.execv()`](https://docs.python.org/3.14/library/os.html#os.execv)) from any thread in which the sub-interpreter happens to be active. Any other value leaves exec unconstrained.

Keep in mind that the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module continues to function even with exec forbidden.

 int allow_threads

Should this be `0`, the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module within the sub-interpreter refrains from spawning threads. Any other value lets threads be created.

 int allow_daemon_threads

Should this be `0`, the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module within the sub-interpreter refrains from spawning daemon threads. Any other value lets daemon threads be created (provided `allow_threads` stays non-zero).

 int check_multi_interp_extensions

With this set to `0`, every extension module — even the legacy single-phase-init ones — is importable from any thread in which the sub-interpreter is active. Any other value restricts importing to multi-phase-init extension modules alone (consult [**PEP 489**](https://peps.python.org/pep-0489/)). (Have a look as well at [`Py_mod_multiple_interpreters`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_multiple_interpreters).)

A value of `1` (non-zero) is mandatory here whenever `use_main_obmalloc` is `0`.

 int gil

Here you dictate how the GIL behaves for the sub-interpreter. The choices available are:

 PyInterpreterConfig_DEFAULT_GIL

Go with the default pick (`PyInterpreterConfig_SHARED_GIL`).

 PyInterpreterConfig_SHARED_GIL

Adopt and share the GIL belonging to the main interpreter.

 PyInterpreterConfig_OWN_GIL

Give the sub-interpreter a GIL all its own.

Whenever this equals `PyInterpreterConfig_OWN_GIL`, a `0` is required for `PyInterpreterConfig.use_main_obmalloc`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](multiple-interpreters-in-a-python-process.md) · [Following source contract](py-newinterpreterfromconfig-to-py-endinterpreter.md)
