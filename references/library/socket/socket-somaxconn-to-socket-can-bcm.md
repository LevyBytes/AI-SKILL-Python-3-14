# socket: `socket.SOMAXCONN`, `socket.AF_CAN`, `socket.PF_CAN`, `socket.CAN_BCM`

socket.SOMAXCONN

 MSG_*

 SOL_*

 SCM_*

 IPPROTO_*

 IPPORT_*

 INADDR_*

 IP_*

 IPV6_*

 EAI_*

 AI_*

 NI_*

 TCP_*

The socket module additionally defines many constants of these forms, the ones documented in the Unix documentation on sockets and/or the IP protocol. They typically appear in arguments to a socket object's `setsockopt()` and `getsockopt()` methods. Usually only the symbols defined in the Unix header files are defined here; for a handful of symbols, default values are supplied.

Changed in version 3.6: `SO_DOMAIN`, `SO_PROTOCOL`, `SO_PEERSEC`, `SO_PASSSEC`, `TCP_USER_TIMEOUT`, `TCP_CONGESTION` were added.

Changed in version 3.6.5: On Windows platforms, support for `TCP_FASTOPEN`, `TCP_KEEPCNT` was added where available.

Changed in version 3.7: `TCP_NOTSENT_LOWAT` was added.

On Windows platforms, support for `TCP_KEEPIDLE`, `TCP_KEEPINTVL` was added where available.

Changed in version 3.10: `IP_RECVTOS` was added. Added `TCP_KEEPALIVE`. On MacOS you can use this constant just as `TCP_KEEPIDLE` is used under Linux.

Changed in version 3.11: Added `TCP_CONNECTION_INFO`. On MacOS you can use this constant just as `TCP_INFO` is used under Linux and BSD.

Changed in version 3.12: Added `SO_RTABLE` and `SO_USER_COOKIE`. Under OpenBSD and FreeBSD respectively, those constants serve the role that `SO_MARK` serves under Linux. Also filled in TCP socket options that had been missing from Linux: `TCP_MD5SIG`, `TCP_THIN_LINEAR_TIMEOUTS`, `TCP_THIN_DUPACK`, `TCP_REPAIR`, `TCP_REPAIR_QUEUE`, `TCP_QUEUE_SEQ`, `TCP_REPAIR_OPTIONS`, `TCP_TIMESTAMP`, `TCP_CC_INFO`, `TCP_SAVE_SYN`, `TCP_SAVED_SYN`, `TCP_REPAIR_WINDOW`, `TCP_FASTOPEN_CONNECT`, `TCP_ULP`, `TCP_MD5SIG_EXT`, `TCP_FASTOPEN_KEY`, `TCP_FASTOPEN_NO_COOKIE`, `TCP_ZEROCOPY_RECEIVE`, `TCP_INQ`, `TCP_TX_DELAY`. Added `IP_PKTINFO`, `IP_UNBLOCK_SOURCE`, `IP_BLOCK_SOURCE`, `IP_ADD_SOURCE_MEMBERSHIP`, `IP_DROP_SOURCE_MEMBERSHIP`.

Changed in version 3.13: Added `SO_BINDTOIFINDEX`. Under Linux this constant plays the role of `SO_BINDTODEVICE`, except it takes a network interface's index rather than its name.

Changed in version 3.14: Filled in the previously missing `IP_FREEBIND`, `IP_RECVERR`, `IPV6_RECVERR`, `IP_RECVTTL`, and `IP_RECVORIGDSTADDR` on Linux.

Changed in version 3.14: On Windows platforms, support for `TCP_QUICKACK` was added where available.

 socket.AF_CAN

 socket.PF_CAN

 SOL_CAN_*

 CAN_*

The socket module additionally defines many constants of these forms, the ones documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.25, NetBSD >= 8.

Added in version 3.3.

Changed in version 3.11: NetBSD support was added.

Changed in version 3.14: Restored missing `CAN_RAW_ERR_FILTER` on Linux.

 socket.CAN_BCM

 CAN_BCM_*

Within the CAN protocol family, CAN_BCM is the broadcast manager (BCM) protocol. The socket module additionally defines the broadcast manager constants documented in the Linux documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.25.

Note

The `CAN_BCM_CAN_FD_FRAME` flag is only available on Linux >= 4.8.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](socket-af-unix-to-socket-sock-nonblock.md) · [Continue](socket-can-raw-fd-frames-to-socket-sol-rds.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md)
