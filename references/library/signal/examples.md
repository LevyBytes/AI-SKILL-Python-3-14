# signal — Examples

### Examples

What follows is a compact demonstration. It leans on the `alarm()` function to cap how long the program will block while opening a file; that matters when the target is a serial device that might be powered off, in which case [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) would otherwise block forever. The trick is to arm a 5-second alarm just before the open; if the open drags on too long, the alarm signal fires and the handler throws an exception.

```python
import signal, os

def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

```

[Subject index](INDEX.md) · [Previous](signal-sigtimedwait.md) · [Continue](note-on-sigpipe.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)
