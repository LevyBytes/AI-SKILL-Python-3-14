import os, time, select, socket, sys
from timer_resources import server_resources

def main():
    with server_resources() as (ep, fds, sock, timeout):
        conn = None
        try:
            conn = None

            is_active = True

            while is_active:
                # Wait for the timer to expire for 3 seconds.
                # epoll.poll() returns a list of (fd, event) pairs.
                # fd is a file descriptor.
                # sock and conn[=returned value of socket.accept()] are socket objects, not file descriptors.
                # So use sock.fileno() and conn.fileno() to get the file descriptors.
                events = ep.poll(timeout)

                # If more than one timer file descriptors are ready for reading at once,
                # epoll.poll() returns a list of (fd, event) pairs.
                #
                # In this example settings,
                #    1st timer fires every 0.25 seconds in 0.25 seconds. (0.25, 0.5, 0.75, 1.0, ...)
                #    2nd timer every 0.5 seconds in 0.5 seconds. (0.5, 1.0, 1.5, 2.0, ...)
                #    3rd timer every 0.75 seconds in 0.75 seconds. (0.75, 1.5, 2.25, 3.0, ...)
                #
                #    In 0.25 seconds, only 1st timer fires.
                #    In 0.5 seconds, 1st timer and 2nd timer fires at once.
                #    In 0.75 seconds, 1st timer and 3rd timer fires at once.
                #    In 1.5 seconds, 1st timer, 2nd timer and 3rd timer fires at once.
                #
                # If a timer file descriptor is signaled more than once since
                # the last os.read() call, os.read() returns the number of signaled
                # as host order of class bytes.
                print(f"Signaled events={events}")
                for fd, event in events:
                    if event & select.EPOLLIN:
                        if fd == sock.fileno():
                            # Check if there is a connection request.
                            print(f"Accepting connection {fd}")
                            client, addr = sock.accept()
                            if conn is not None:
                                client.close()
                                continue
                            conn = client
                            conn.setblocking(False)
                            print(f"Accepted connection {conn} from {addr}")
                            ep.register(conn, select.EPOLLIN)
                        elif conn and fd == conn.fileno():
                            # Check if there is data to read.
                            print(f"Reading data {fd}")
                            try:
                                data = conn.recv(1024)
                            except BlockingIOError:
                                continue
                            if data:
                                # Invalid UTF-8 is treated as an unrecognized command.
                                cmd = data.decode(errors="replace")
                                if cmd.startswith("stop"):
                                    print(f"Stopping server")
                                    is_active = False
                                else:
                                    print(f"Unknown command: {cmd}")
                            else:
                                # No more data, close connection
                                print(f"Closing connection {fd}")
                                ep.unregister(conn)
                                conn.close()
                                conn = None
                        elif fd in fds:
                            print(f"Reading timer {fd}")
                            count = int.from_bytes(os.read(fd, 8), byteorder=sys.byteorder)
                            print(f"Timer {fds.index(fd) + 1} expired {count} times")
                        else:
                            print(f"Unknown file descriptor {fd}")
        finally:
            if conn is not None:
                conn.close()

if __name__ == "__main__":
    main()
