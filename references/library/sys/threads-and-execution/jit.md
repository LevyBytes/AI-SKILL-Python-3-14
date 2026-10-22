# sys._jit

sys._jit

Tools for inspecting just-in-time compilation.

**CPython implementation detail:** JIT compilation is an *experimental implementation detail* of CPython. There is no guarantee that `sys._jit` exists or acts identically across all Python implementations, versions, or build configurations.

Added in version 3.14.

 _jit.is_available()

Return `True` when the running Python executable has support for JIT compilation, and `False` if it does not. You govern this by building CPython with the `--experimental-jit` option on Windows, and with the [`--enable-experimental-jit`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-experimental-jit) option on every other platform.

 _jit.is_enabled()

Return `True` when JIT compilation has been switched on for the active Python process (which implies `sys._jit.is_available()`), and `False` if not. Provided JIT compilation is available, you steer this by assigning the [`PYTHON_JIT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_JIT) environment variable a value of `0` (disabled) or `1` (enabled) when the interpreter starts up.

 _jit.is_active()

Return `True` when the uppermost Python frame is at present running JIT code (which implies `sys._jit.is_enabled()`), and `False` if not.

Note

The purpose of this function is to test and debug the JIT itself. Refrain from using it for anything else.

Note

Because of how tracing JIT compilers operate, calling this function more than once can produce surprising outcomes. As an illustration, branching based on its return value will probably trigger unexpected behavior (when doing so makes JIT code be entered or left):

```pycon
>>> for warmup in range(BIG_NUMBER):
...     # This line is "hot", and is eventually JIT-compiled:
...     if sys._jit.is_active():
...         # This line is "cold", and is run in the interpreter:
...         assert sys._jit.is_active()
...
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
    assert sys._jit.is_active()
           ~~~~~~~~~~~~~~~~~~^^
AssertionError

```

[API family](INDEX.md) · [sys context index](../INDEX.md).
