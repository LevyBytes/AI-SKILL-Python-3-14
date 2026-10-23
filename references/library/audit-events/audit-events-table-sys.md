# Audit events table - sys

| Audit event | Arguments | References |
| --- | --- | --- |
| sys._current_exceptions |  | [1] |
| sys._current_frames |  | [1] |
| sys._getframe | `frame` | [1] |
| sys._getframemodulename | `depth` | [1] |
| sys.addaudithook |  | [1][2] |
| sys.excepthook | `hook`, `type`, `value`, `traceback` | [1] |
| sys.monitoring.register_callback | `func` | [1] |
| sys.remote_exec | `pid` | [1] |
| sys.set_asyncgen_hooks_finalizer |  | [1] |
| sys.set_asyncgen_hooks_firstiter |  | [1] |
| sys.setprofile |  | [1] |
| sys.settrace |  | [1] |
| sys.unraisablehook | `hook`, `unraisable` | [1] |

[Subject index](INDEX.md) · [Previous](audit-events-table-subprocess.md) · [Continue](audit-events-table-syslog.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)
