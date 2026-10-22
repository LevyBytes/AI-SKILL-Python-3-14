# Periodic timerfd example and nanosecond/epoll setup

### Examples

In the example below, a timer file descriptor is used to run a function twice every second:

```python
# Practical scripts should use really use a non-blocking timer,
# we use a blocking timer here for simplicity.
import os, time

# Create the timer file descriptor
fd = os.timerfd_create(time.CLOCK_REALTIME)

# Start the timer in 1 second, with an interval of half a second
os.timerfd_settime(fd, initial=1, interval=0.5)

try:
    # Process timer events four times.
    for _ in range(4):
        # read() will block until the timer expires
        _ = os.read(fd, 8)
        print("Timer expired")
finally:
    # Remember to close the timer file descriptor!
    os.close(fd)

```

Timer file descriptors sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type introduces: the `_ns` variants of the functions let you give the initial expiration and the interval as integer nanoseconds.

Here, [`epoll()`](https://docs.python.org/3.14/library/select.html#select.epoll) is paired with timer file descriptors to block until the file descriptor becomes readable:

[Subject index](INDEX.md) · [Imports, epoll, socket and timer setup](imports-epoll-socket-and-timer-setup.md) · [Whole polling try/finally and timer cleanup](whole-polling-try-finally-and-timer-cleanup.md) · [Complete timerfd select example](complete-timerfd-select-example.md) · [Previous source context](timer-file-descriptor-howto.md) · [Following source context](imports-epoll-socket-and-timer-setup.md)
