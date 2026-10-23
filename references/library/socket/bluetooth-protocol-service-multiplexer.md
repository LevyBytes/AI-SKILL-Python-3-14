# socket - Socket families - Contract: `psm` is an integer holding the Protocol/Service Multiplexer.

`psm` is an integer holding the Protocol/Service Multiplexer.

    - `cid` is an optional integer holding the Channel Identifier; when omitted, it defaults to zero.

    - `bdaddr_type` is an optional integer giving the address type — one of `BDADDR_BREDR` (default), `BDADDR_LE_PUBLIC`, `BDADDR_LE_RANDOM`.

Changed in version 3.14: Added `cid` and `bdaddr_type` fields.

  - `BTPROTO_RFCOMM` takes `(bdaddr, channel)`, in which `bdaddr` gives the Bluetooth address as a string and `channel` is an integer.

  - `BTPROTO_HCI` takes a format that varies with your OS.

    - Under Linux it takes either an integer `device_id` or a tuple `(device_id, [channel])`, where `device_id` names the Bluetooth device's number and `channel` is an optional integer naming the HCI channel (`HCI_CHANNEL_RAW` by default).

    - Under FreeBSD, NetBSD and DragonFly BSD it takes `bdaddr`, where `bdaddr` gives the Bluetooth address as a string.

Changed in version 3.2: NetBSD and DragonFlyBSD support added.

Changed in version 3.13.3: FreeBSD support added.

Changed in version 3.14: Added `channel` field. A bare `device_id` outside any tuple is now accepted.

  - `BTPROTO_SCO` takes `bdaddr`, where `bdaddr` gives the Bluetooth address as a string or as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. (ex. `'12:23:34:45:56:67'` or `b'12:23:34:45:56:67'`)

Changed in version 3.14: FreeBSD support added.

- `AF_ALG` is a Linux-only, socket-based gateway into Kernel cryptography. You set up an algorithm socket using a tuple of two to four elements `(type, name [, feat [, mask]])`, where:

  - *type* is the algorithm type as string, e.g. `aead`, `hash`, `skcipher` or `rng`.

  - *name*, given as a string, is the name of the algorithm together with its operation mode, e.g. `sha256`, `hmac(sha256)`, `cbc(aes)` or `drbg_nopr_ctr_aes256`.

  - *feat* and *mask* are unsigned 32bit integers.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.38.

Some algorithm types require more recent Kernels.

Added in version 3.6.

- `AF_VSOCK` lets virtual machines and their hosts communicate. A `(CID, port)` tuple represents the sockets, where the context ID (or CID) and the port are both integers.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.9

See *[vsock(7)](https://manpages.debian.org/vsock(7))*

Added in version 3.7.

- `AF_PACKET` is a low-level interface reaching network devices directly. A tuple `(ifname, proto[, pkttype[, hatype[, addr]]])` represents the addresses, where:

  - *ifname* - String specifying the device name.

  - *proto* - The Ethernet protocol number. It may be `ETH_P_ALL` to grab every protocol, one of the ETHERTYPE_* constants, or any other Ethernet protocol number.

[Subject index](INDEX.md) · [Previous](socket-families-section-introduction-and-initial-examples.md) · [Continue](packet-socket-address-type-contract.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Socket families](socket-families-section-introduction-and-initial-examples.md)
