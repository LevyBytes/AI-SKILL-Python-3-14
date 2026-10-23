# Complete conditional logging decorator demonstration

What the script does is set things up so that `foo` is wrapped by a decorator that performs the conditional logging we need. That decorator accepts a logger argument and, while the wrapped function runs, hooks up a memory handler. You can further configure the decorator by supplying a target handler, the level that triggers a flush, and how many records the buffer can hold before flushing. When omitted, these fall back to a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) that emits to `sys.stderr`, `logging.ERROR` and `100` in that order.

Here's the script:

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/logging-cookbook.html#buffering-logging-messages-and-outputting-them-conditionally).

[Subject index](INDEX.md) · [Previous source owning section](buffering-logging-messages-and-outputting-them-conditionally.md) · [Conditional buffer flush output and decorator syntax](conditional-buffer-flush-output-and-decorator-syntax.md) · [Following source context](conditional-buffer-flush-output-and-decorator-syntax.md)
