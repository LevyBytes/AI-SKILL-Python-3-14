# threading: `threading.Event`

### Event objects

This ranks among the simplest ways for threads to communicate: one thread raises an event and other threads wait on it.

An event object keeps an internal flag that the `set()` method can turn true and the `clear()` method can turn back false. The `wait()` method blocks while the flag stays false.

 *class *threading.Event

Class that provides event objects. An event keeps a flag that the `set()` method can turn true and the `clear()` method can turn back false. The `wait()` method blocks while the flag stays false. The flag begins false.

Changed in version 3.3: was previously a factory function, and is now a class.

[Subject index](INDEX.md) · [Previous](semaphore-example.md) · [Continue](threading-event-is-set-to-threading-event-wait.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
