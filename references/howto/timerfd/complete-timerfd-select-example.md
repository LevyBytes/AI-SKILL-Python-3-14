# Complete timerfd select example

Here, [`select()`](https://docs.python.org/3.14/library/select.html#select.select) is paired with timer file descriptors to block until the file descriptor becomes readable:

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/timerfd.html#examples).

[Subject index](INDEX.md) · [Periodic timerfd example and nanosecond/epoll setup](periodic-timerfd-example-and-nanosecond-epoll-setup.md) · [Imports, epoll, socket and timer setup](imports-epoll-socket-and-timer-setup.md) · [Whole polling try/finally and timer cleanup](whole-polling-try-finally-and-timer-cleanup.md) · [Previous source context](whole-polling-try-finally-and-timer-cleanup.md)
