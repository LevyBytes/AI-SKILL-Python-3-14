# socket: Windows socket controls, virtual sockets and Bluetooth addressing

socket.SIO_RCVALL

 socket.SIO_KEEPALIVE_VALS

 socket.SIO_LOOPBACK_FAST_PATH

 RCVALL_*

Constants for Windows' WSAIoctl(). They serve as arguments to a socket object's `ioctl()` method.

Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

 TIPC_*

TIPC related constants, mirroring those the C socket API exports. Consult the TIPC documentation for more information.

 socket.AF_ALG

 socket.SOL_ALG

 ALG_*

Constants for Linux Kernel cryptography.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.38.

Added in version 3.6.

 socket.AF_VSOCK

 socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID

 VMADDR*

 SO_VM*

Constants for Linux host/guest communication.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.8.

Added in version 3.7.

 socket.AF_LINK

[Availability](https://docs.python.org/3.14/library/intro.html#availability): BSD, macOS.

Added in version 3.4.

 socket.has_ipv6

This constant holds a boolean value that tells whether this platform supports IPv6.

 socket.AF_BLUETOOTH

 socket.BTPROTO_L2CAP

 socket.BTPROTO_RFCOMM

 socket.BTPROTO_HCI

 socket.BTPROTO_SCO

Integer constants for use with Bluetooth addresses.

 socket.BDADDR_ANY

 socket.BDADDR_LOCAL

These string constants hold Bluetooth addresses that carry special meanings. As an example, `BDADDR_ANY` can stand for any address when you specify the binding socket with `BTPROTO_RFCOMM`.

 socket.BDADDR_BREDR

 socket.BDADDR_LE_PUBLIC

 socket.BDADDR_LE_RANDOM

These constants give the Bluetooth address type used when you bind or connect a `BTPROTO_L2CAP` socket.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux, FreeBSD

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](socket-can-raw-fd-frames-to-socket-sol-rds.md) · [Continue](socket-sol-rfcomm-to-socket-so-hci-pkt-filter.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md)
