# Event: `wait()`, `set()`, `clear()`, `is_set()`

*async *wait()

Hold off until the event has been set.

When the event is already set, give back `True` right away. Failing that, stay blocked until some other task invokes `set()`.

 set()

Set the event.

Every task that was waiting on the event being set is woken up at once.

 clear()

Clear (unset) the event.

From here on, tasks that wait via `wait()` will stay blocked until `set()` is invoked once more.

 is_set()

Give back `True` whenever the event is set.

[Subject index](INDEX.md) · [Previous](asyncio-event-class.md) · [Continue](asyncio-condition-class.md) · [Owning module, declaration or section: asyncio.Event](asyncio-event-class.md) · [Owning module, declaration or section: Event](asyncio-event-class.md)
