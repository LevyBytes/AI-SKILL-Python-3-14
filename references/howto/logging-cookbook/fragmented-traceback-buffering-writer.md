# Fragmented traceback writes and BufferingLoggerWriter correction

Be aware that under the scheme above you depend to some degree on buffering and on the order of the write calls you intercept. Take the `LoggerWriter` definition above: if you run the snippet

```python
sys.stderr = LoggerWriter(logger, logging.WARNING)
1 / 0

```

then executing the script produces

```text
WARNING:demo:Traceback (most recent call last):

WARNING:demo:  File "/home/runner/cookbook-loggerwriter/test.py", line 53, in <module>

WARNING:demo:
WARNING:demo:main()
WARNING:demo:  File "/home/runner/cookbook-loggerwriter/test.py", line 49, in main

WARNING:demo:
WARNING:demo:1 / 0
WARNING:demo:ZeroDivisionError
WARNING:demo::
WARNING:demo:division by zero

```

This output, as you can tell, leaves something to be desired. The reason is that the underlying code writing to `sys.stderr` performs several writes, and each one yields its own logged line (the final three lines above being an example). Buffering is the way around this: hold the data and emit log lines only once newlines turn up. Consider a somewhat improved `LoggerWriter`:

```python
class BufferingLoggerWriter(LoggerWriter):
    def __init__(self, logger, level):
        super().__init__(logger, level)
        self.buffer = ''

    def write(self, message):
        if '\n' not in message:
            self.buffer += message
        else:
            parts = message.split('\n')
            if self.buffer:
                s = self.buffer + parts.pop(0)
                self.logger.log(self.level, s)
            self.buffer = parts.pop()
            for part in parts:
                self.logger.log(self.level, part)

```

This simply accumulates content until a newline appears, then logs whole lines. That approach gives you cleaner output:

```text
WARNING:demo:Traceback (most recent call last):
WARNING:demo:  File "/home/runner/cookbook-loggerwriter/main.py", line 55, in <module>
WARNING:demo:    main()
WARNING:demo:  File "/home/runner/cookbook-loggerwriter/main.py", line 52, in main
WARNING:demo:    1/0
WARNING:demo:ZeroDivisionError: division by zero

```

[Subject index](INDEX.md) · [LoggerWriter file-like adapter and stdout/stderr routing](loggerwriter-file-like-adapter-and-stdout-stderr-routing.md) · [Previous source context](loggerwriter-file-like-adapter-and-stdout-stderr-routing.md) · [Following source context](how-to-uniformly-handle-newlines-in-logging-output.md)
