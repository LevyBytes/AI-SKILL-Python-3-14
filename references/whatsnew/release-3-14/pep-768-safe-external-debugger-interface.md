# What's new in Python 3.14 / **PEP 768**: Safe external debugger interface — sys

### [**PEP 768**](https://peps.python.org/pep-0768/): Safe external debugger interface

A zero-overhead debugging interface arrives with Python 3.14, letting debuggers and profilers latch onto live Python processes safely, with no need to halt or relaunch them. It marks a meaningful upgrade to Python's debugging toolkit, so the previous unsafe workarounds are no longer needed.

What the new interface offers is safe attachment points for injecting debugger code, all without touching the interpreter's ordinary execution path or imposing any runtime cost. As a result, tooling can examine and engage with Python applications live — an essential ability for production deployments and high-availability systems.

As a convenience, the [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec) function delivers this interface. To illustrate:

```python
import sys
from tempfile import NamedTemporaryFile

with NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    script_path = f.name
    f.write(f'import my_debugger; my_debugger.connect({os.getpid()})')

# Execute in process with PID 1234
print('Behold! An offering:')
sys.remote_exec(1234, script_path)

```

With this function you can dispatch Python code into a target process to run at its next safe execution point. Tool authors are also free to code the protocol themselves following the PEP, which spells out the inner workings behind safely attaching to live processes.

Security was front of mind throughout the design of this debugging interface, which bundles a number of knobs for governing access:

- A [`PYTHON_DISABLE_REMOTE_DEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_DISABLE_REMOTE_DEBUG) environment variable.

- A [`-X disable-remote-debug`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option.

- A [`--without-remote-debug`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-remote-debug) configure flag to completely disable the feature at build time.

(Contributed by Pablo Galindo Salgado, Matt Wozniski, and Ivona Stojanovic in [gh-131591](https://github.com/python/cpython/issues/131591).)

See also

[**PEP 768**](https://peps.python.org/pep-0768/).

[Subject index](INDEX.md) · [Previous source section](pep-750-template-string-literals.md) · [Next source section](a-new-type-of-interpreter.md) · [Release/subject declaration](summary-release-highlights.md)
