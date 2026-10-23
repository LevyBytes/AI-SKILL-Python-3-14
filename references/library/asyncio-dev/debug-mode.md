# asyncio - Debug Mode

### Debug Mode

Out of the box asyncio operates in production mode. To make development smoother, asyncio offers a *debug mode*.

You can switch on asyncio debug mode through any of these routes:

- Giving the [`PYTHONASYNCIODEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) environment variable a value of `1`.

- Using the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode).

- Passing `debug=True` to [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run).

- Calling [`loop.set_debug()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_debug).

Beyond turning the debug mode on, you might also want to:

- push the asyncio logger’s log level up to [`logging.DEBUG`](https://docs.python.org/3.14/library/logging.html#logging.DEBUG); as an illustration, this bit of code might run when your application starts:

```python
logging.basicConfig(level=logging.DEBUG)

```

- set up the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module so it shows [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) warnings. You can pull that off, for instance, with the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) `default` command line option.

Once the debug mode is switched on:

- A lot of asyncio APIs that aren’t threadsafe — the [`loop.call_soon()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon) and [`loop.call_at()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_at) methods among them — will throw an exception should you invoke them off the wrong thread.

- Should an I/O operation drag on too long, the I/O selector’s execution time gets written to the log.

- Any callback running past 100 milliseconds gets logged. You can adjust the [`loop.slow_callback_duration`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.slow_callback_duration) attribute to define, in seconds, the shortest run time that counts as “slow”.

[Subject index](INDEX.md) · [Previous](developing-with-asyncio.md) · [Continue](concurrency-and-multithreading.md)
