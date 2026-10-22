# socket: CAN protocols, packet capture and reliable datagrams

socket.CAN_RAW_FD_FRAMES

Turns on CAN FD support inside a CAN_RAW socket, which is off by default. With it your application can send both CAN and CAN FD frames; bear in mind, though, that when reading from the socket you have to accept both CAN and CAN FD frames.

This constant is documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.6.

Added in version 3.5.

 socket.CAN_RAW_JOIN_FILTERS

Joins the applied CAN filters so that only CAN frames matching every one of the supplied CAN filters reach user space.

This constant is documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.1.

Added in version 3.9.

 socket.CAN_ISOTP

Within the CAN protocol family, CAN_ISOTP is the ISO-TP (ISO 15765-2) protocol. The ISO-TP constants are documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.25.

Added in version 3.7.

 socket.CAN_J1939

Within the CAN protocol family, CAN_J1939 is the SAE J1939 protocol. The J1939 constants are documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 5.4.

Added in version 3.9.

 socket.AF_DIVERT

 socket.PF_DIVERT

The socket module additionally defines these two constants, the ones documented in the FreeBSD divert(4) manual page.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD >= 14.0.

Added in version 3.12.

 socket.AF_PACKET

 socket.PF_PACKET

 PACKET_*

The socket module additionally defines many constants of these forms, the ones documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.2.

 socket.ETH_P_ALL

`ETH_P_ALL` may be passed as *proto* to the `socket` constructor for the `AF_PACKET` family so as to capture every packet, no matter the protocol.

For more information, see the *[packet(7)](https://manpages.debian.org/packet(7))* manpage.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux.

Added in version 3.12.

 socket.AF_RDS

 socket.PF_RDS

 socket.SOL_RDS

 RDS_*

The socket module additionally defines many constants of these forms, the ones documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.30.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](socket-somaxconn-to-socket-can-bcm.md) · [Continue](socket-sio-rcvall-to-socket-bdaddr-le-random.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md)
