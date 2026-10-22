# -X disable_remote_debug

- `-X disable_remote_debug` turns off the remote debugging support outlined in [**PEP 768**](https://peps.python.org/pep-0768/). That covers both the ability to schedule code to run in a separate process and the ability to receive code for running in the present process.

The option exists only on certain platforms and does nothing where the current system lacks support. See also `PYTHON_DISABLE_REMOTE_DEBUG` and [**PEP 768**](https://peps.python.org/pep-0768/).

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](x-perf-jit.md) · [Following source section](x-cpu-count-n.md)
