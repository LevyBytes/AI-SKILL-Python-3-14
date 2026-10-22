# threading: `threading.Timer`

### Timer objects

This class stands for an action meant to run only once a set span of time has elapsed — a timer. `Timer` derives from `Thread` and as such doubles as an example of building custom threads.

Like threads, timers are started by invoking their `Timer.start` method. You can halt the timer (before its action has started) by invoking the `cancel()` method. The span the timer waits before carrying out its action may not match the span the user gave exactly.

For example:

```python
def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed

```

 *class *threading.Timer(*interval*, *function*, *args=None*, *kwargs=None*)

Build a timer that runs *function* with arguments *args* and keyword arguments *kwargs*, once *interval* seconds have elapsed. When *args* is `None` (the default) an empty list gets used. When *kwargs* is `None` (the default) an empty dict gets used.

Changed in version 3.3: was previously a factory function, and is now a class.

[Subject index](INDEX.md) · [Previous](threading-event-is-set-to-threading-event-wait.md) · [Continue](threading-timer-cancel.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
