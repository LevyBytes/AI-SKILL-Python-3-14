# socket: Bluetooth HCI channels and local-socket options

Changed in version 3.14: On NetBSD plus DragonFly BSD, `SO_HCI_EVT_FILTER` and `SO_HCI_PKT_FILTER` were introduced. Across FreeBSD, NetBSD, and DragonFly BSD, `HCI_DATA_DIR` was introduced.

 socket.HCI_DEV_NONE

The `device_id` value passed when opening an HCI socket that is not tied to any particular Bluetooth adapter.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux

Added in version 3.14.

 socket.HCI_CHANNEL_RAW

 socket.HCI_CHANNEL_USER

 socket.HCI_CHANNEL_MONITOR

 socket.HCI_CHANNEL_CONTROL

 socket.HCI_CHANNEL_LOGGING

Allowed settings for the `channel` field within a `BTPROTO_HCI` address.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux

Added in version 3.14.

 socket.AF_QIPCRTR

A constant for the Qualcomm IPC router protocol, employed for talking to a service that exposes remote processors.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.7.

 socket.SCM_CREDS2

 socket.LOCAL_CREDS

 socket.LOCAL_CREDS_PERSISTENT

Both LOCAL_CREDS and LOCAL_CREDS_PERSISTENT work with SOCK_DGRAM and SOCK_STREAM sockets and mirror the Linux/DragonFlyBSD SO_PASSCRED behaviour; LOCAL_CREDS transmits the credentials on the initial read, whereas LOCAL_CREDS_PERSISTENT does so on every read, in which case SCM_CREDS2 has to serve as the message type for that latter mode.

Added in version 3.11.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD.

 socket.SO_INCOMING_CPU

Constant for improving CPU locality, meant to be paired with `SO_REUSEPORT`.

Added in version 3.11.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.9

 socket.SO_REUSEPORT_LB

>

Constant that permits binding duplicate addresses and ports while load balancing across them.

Added in version 3.14.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD >= 12.0

[Subject index](INDEX.md) · [Continue](socket-af-hyperv-to-socket-shut-rdwr.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md) · [Owning module, declaration or section: HCI_FILTER, HCI_TIME_STAMP, HCI_DATA_DIR, SO_HCI_EVT_FILTER and SO_HCI_PKT_FILTER](socket-sol-rfcomm-to-socket-so-hci-pkt-filter.md) · [Preceding source contract and version conditions](socket-sol-rfcomm-to-socket-so-hci-pkt-filter.md)
