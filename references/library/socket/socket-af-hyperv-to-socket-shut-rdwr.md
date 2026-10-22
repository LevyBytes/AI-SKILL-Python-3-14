# socket: Hyper-V sockets, Ethernet types and shutdown constants

socket.AF_HYPERV

 socket.HV_PROTOCOL_RAW

 socket.HVSOCKET_CONNECT_TIMEOUT

 socket.HVSOCKET_CONNECT_TIMEOUT_MAX

 socket.HVSOCKET_CONNECTED_SUSPEND

 socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU

 socket.HV_GUID_ZERO

 socket.HV_GUID_WILDCARD

 socket.HV_GUID_BROADCAST

 socket.HV_GUID_CHILDREN

 socket.HV_GUID_LOOPBACK

 socket.HV_GUID_PARENT

Constants for Windows Hyper-V sockets used in host/guest communication.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.12.

 socket.ETHERTYPE_ARP

 socket.ETHERTYPE_IP

 socket.ETHERTYPE_IPV6

 socket.ETHERTYPE_VLAN

[IEEE 802.3 protocol number](https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.txt). constants.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux, FreeBSD, macOS.

Added in version 3.12.

 socket.SHUT_RD

 socket.SHUT_WR

 socket.SHUT_RDWR

The `shutdown()` method on socket objects relies on these constants.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

[Subject index](INDEX.md) · [Previous](socket-hci-dev-none-to-socket-so-reuseport-lb.md) · [Continue](socket-socketpair-to-socket-fromshare.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md)
