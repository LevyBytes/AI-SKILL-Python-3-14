# When to use `PYTHON_DISABLE_REMOTE_DEBUG`

### When to use `PYTHON_DISABLE_REMOTE_DEBUG`

By means of the [`PYTHON_DISABLE_REMOTE_DEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_DISABLE_REMOTE_DEBUG) environment variable (or its counterpart, the [`-X disable_remote_debug`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) flag), operators can switch off the protocol's in-process half as a **defence-in-depth** step. It can pay off in locked-down or sandboxed deployments where nobody intends to debug or profile the process and shrinking the attack surface is what counts — even granting that OS-level privilege checks already bar unprivileged access.

Assigning this variable leaves the other OS-level debugging interfaces (`ptrace`, `/proc`, `task_for_pid`, and so on) **not** affected; each stays usable under its own permission model.

[Subject index](INDEX.md) · [Previous source context](security-and-threat-model.md)
