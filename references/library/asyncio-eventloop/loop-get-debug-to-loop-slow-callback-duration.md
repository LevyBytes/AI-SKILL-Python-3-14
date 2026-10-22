# Enabling debug mode

### Enabling debug mode

 loop.get_debug()

Retrieve the event loop's debug mode flag ([`bool`](https://docs.python.org/3.14/library/functions.html#bool)).

It defaults to `True` whenever the [`PYTHONASYNCIODEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) environment variable holds a non-empty string, and `False` in every other case.

 loop.set_debug(*enabled: [bool](https://docs.python.org/3.14/library/functions.html#bool)*)

Turn the event loop's debug mode on or off.

Changed in version 3.7: Turning debug mode on is now possible through the new [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) as well.

 loop.slow_callback_duration

Use this attribute to define, in seconds, the shortest run time that counts as “slow”. With debug mode active, callbacks crossing that threshold get logged as “slow”.

Default value is 100 milliseconds.

See also

The [debug mode of asyncio](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-debug-mode).

[Subject index](INDEX.md) · [Previous](loop-set-exception-handler-to-loop-call-exception-handler.md) · [Continue](running-subprocesses.md)
