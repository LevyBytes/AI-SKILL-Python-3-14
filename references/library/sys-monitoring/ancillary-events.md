# sys.monitoring — Ancillary events

### Ancillary events

Ancillary events can be watched just like the rest, but their control comes from another event:

- `C_RAISE`

- `C_RETURN`

The `CALL` event governs the `C_RETURN` and `C_RAISE` events. You will only observe `C_RETURN` and `C_RAISE` events when the matching `CALL` event is under observation.

[Subject index](INDEX.md) · [Previous](deprecated-event.md) · [Continue](other-events.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
