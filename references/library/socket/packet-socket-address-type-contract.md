# socket - Socket families - Contract: *pkttype* - Optional integer giving the packet type:

- *pkttype* - Optional integer giving the packet type:

    - `PACKET_HOST` (the default) - A packet addressed to the local host.

    - `PACKET_BROADCAST` - A physical-layer broadcast packet.

    - `PACKET_MULTICAST` - A packet sent to a physical-layer multicast address.

    - `PACKET_OTHERHOST` - A packet bound for another host that a device driver in promiscuous mode happened to catch.

    - `PACKET_OUTGOING` - A packet that left the local host and was looped back to a packet socket.

  - *hatype* - Optional integer giving the ARP hardware address type.

  - *addr* - Optional bytes-like object giving the hardware physical address, whose meaning hinges on the device.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.2.

- `AF_QIPCRTR` is a Linux-only, socket-based interface used to talk to services that run on co-processors within Qualcomm platforms. A `(node, port)` tuple represents the address family, where the *node* and *port* are both non-negative integers.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.7.

Added in version 3.8.

- `IPPROTO_UDPLITE` is a UDP variant that lets you say how much of a packet the checksum spans. It introduces two socket options you can adjust. Calling `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_SEND_CSCOV, length)` changes how much of each outgoing packet the checksum covers, while `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_RECV_CSCOV, length)` screens out packets that cover too little of their data. For both, `length` should be in `range(8, 2**16, 8)`.

Build such a socket with `socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv4 or with `socket(AF_INET6, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv6.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.20, FreeBSD >= 10.1

Added in version 3.9.

- `AF_HYPERV` is a Windows-only, socket-based interface used to talk to Hyper-V hosts and guests. A `(vm_id, service_id)` tuple represents the address family, where the `vm_id` and `service_id` are UUID strings.

The `vm_id` is either the virtual machine identifier or one of a set of known VMID values used when the target is not a specific virtual machine. The known VMID constants that `socket` defines are:

  -

[Subject index](INDEX.md) · [Previous](bluetooth-protocol-service-multiplexer.md) · [Continue](socket-families.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Socket families](socket-families-section-introduction-and-initial-examples.md)
