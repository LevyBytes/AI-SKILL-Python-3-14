# Buffering logging messages and outputting them conditionally

### Buffering logging messages and outputting them conditionally

There may be cases where you'd like to record messages in a temporary store and emit them only when a particular condition arises. For instance, you might begin logging debug events inside a function, and should the function finish error-free, you'd rather not clutter the log with the gathered debug information, yet if an error occurs you want the whole of the debug information emitted alongside the error.

Below is an example showing how you could achieve this with a decorator on the functions where you want logging to act this way. It relies on the [`logging.handlers.MemoryHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.MemoryHandler), which permits buffering logged events until some condition occurs, whereupon the buffered events are `flushed` - handed off to a second handler (the `target` handler) for processing. By default the `MemoryHandler` flushed once its buffer fills or an event whose level meets or exceeds a given threshold appears. You can apply this recipe with a more specialised subclass of `MemoryHandler` should you want custom flushing behavior.

The example script holds a simple function, `foo`, which merely runs through every logging level, writing to `sys.stderr` to announce the level it's about to log at, then actually logging a message at that level. You can hand `foo` a parameter which, when true, makes it log at ERROR and CRITICAL levels - otherwise it logs only at DEBUG, INFO and WARNING levels.

[Subject index](INDEX.md) · [Following source continuation](complete-conditional-logging-decorator-demonstration.md) · [Previous source context](speaking-logging-messages.md)
