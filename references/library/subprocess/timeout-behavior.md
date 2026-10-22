# subprocess — Timeout Behavior

### Notes

### Timeout Behavior

Anyone reaching for the `timeout` parameter in functions such as `run()`, `Popen.wait()`, or `Popen.communicate()` ought to keep the behaviours below in mind:

1.

**Process Creation Delay**: On a good many platform APIs, the act of creating the process to begin with cannot be cut short. So even with a timeout in place, no timeout exception is assured until at least the full duration of process creation has elapsed.

2.

**Extremely Small Timeout Values**: Handing in tiny timeout values — a few milliseconds, say — can produce `TimeoutExpired` exceptions almost at once, since process creation and system scheduling each take time by their very nature.

[Subject index](INDEX.md) · [Continue](converting-an-argument-sequence-to-a-string-on-windows.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
