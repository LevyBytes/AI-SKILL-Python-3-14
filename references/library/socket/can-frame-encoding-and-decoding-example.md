# socket: CAN frame packing and socket address reuse

```python
import socket
import struct

# CAN frame packing/unpacking (see 'struct can_frame' in <linux/can.h>)

can_frame_fmt = "=IB3x8s"
can_frame_size = struct.calcsize(can_frame_fmt)

def build_can_frame(can_id, data):
    can_dlc = len(data)
    data = data.ljust(8, b'\x00')
    return struct.pack(can_frame_fmt, can_id, can_dlc, data)

def dissect_can_frame(frame):
    can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
    return (can_id, can_dlc, data[:can_dlc])

# create a raw socket and bind it to the 'vcan0' interface
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',))

while True:
    cf, addr = s.recvfrom(can_frame_size)

    print('Received: can_id=%x, can_dlc=%x, data=%s' % dissect_can_frame(cf))

    try:
        s.send(cf)
    except OSError:
        print('Error sending CAN frame')

    try:
        s.send(build_can_frame(0x01, b'\x01\x02\x03'))
    except OSError:
        print('Error sending CAN frame')

```

Re-running an example a few times with too little gap between runs can bring on this error:

```python
OSError: [Errno 98] Address already in use

```

That happens because the earlier run has left the socket sitting in a `TIME_WAIT` state, so it can't be reused right away.

To head this off, there's a `socket` flag you can set, namely `socket.SO_REUSEADDR`:

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

```

the `SO_REUSEADDR` flag instructs the kernel to take a local socket still in `TIME_WAIT` state back into use, skipping the wait for its normal timeout to lapse.

See also

For a primer on socket programming (in C), take a look at these papers:

- *An Introductory 4.3BSD Interprocess Communication Tutorial*, by Stuart Sechrest

- *An Advanced 4.3BSD Interprocess Communication Tutorial* — authored by Samuel J. Leffler and colleagues,

which you'll find in the UNIX Programmer’s Manual, Supplementary Documents 1 — specifically at sections PS1:7 and PS1:8. Reference material that is platform-specific, covering the assorted socket-related system calls, likewise makes a worthwhile source on the finer points of socket semantics. On Unix, turn to the manual pages; on Windows, consult the WinSock (or Winsock 2) specification. For IPv6-ready APIs, readers might look to [**RFC 3493**](https://datatracker.ietf.org/doc/html/rfc3493.html) titled Basic Socket Interface Extensions for IPv6.

[Subject index](INDEX.md) · [Previous](example-code-example-import-socket-continue-to-break.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Example](example-section-introduction-and-initial-examples.md)
