# sys.monitoring — `sys.monitoring` — Execution event monitoring

### `sys.monitoring` — Execution event monitoring

Added in version 3.12.

---

Note

Within the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module, `sys.monitoring` is a namespace rather than a standalone module, so `import sys.monitoring` would blow up with a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError). The right approach is to `import sys` and then reach for `sys.monitoring`.

The functions and constants you need to switch event monitoring on and steer it are exposed through this namespace.

While programs run, events arise that tools watching execution might care about. Receiving callbacks when events worth noting take place is something the `sys.monitoring` namespace makes possible.

Three components make up the monitoring API:

- Tool identifiers

- Events

- Callbacks

[Subject index](INDEX.md) · [Previous](execution-event-monitoring.md) · [Continue](tool-identifiers.md)
