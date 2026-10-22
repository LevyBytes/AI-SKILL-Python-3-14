import os
import select
import socket
import time
from contextlib import ExitStack, contextmanager

@contextmanager
def server_resources():
    with ExitStack() as cleanup:
        ep = select.epoll()
        cleanup.callback(ep.close)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cleanup.callback(sock.close)
        sock.bind(("127.0.0.1", 1234))
        sock.setblocking(False)
        sock.listen(1)
        ep.register(sock, select.EPOLLIN)
        fds = []
        for _ in range(3):
            fd = os.timerfd_create(time.CLOCK_REALTIME, flags=os.TFD_NONBLOCK)
            cleanup.callback(os.close, fd)
            fds.append(fd)
            ep.register(fd, select.EPOLLIN)
        for i, fd in enumerate(fds, start=1):
            interval = i * 10**9 // 4
            os.timerfd_settime_ns(fd, initial=interval, interval=interval)
        yield ep, fds, sock, 3
