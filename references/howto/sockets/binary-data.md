# Binary Data

### Binary Data

Shipping binary data across a socket is entirely doable. The snag is that machines don't all agree on how binary data is laid out. To take one case, [network byte order](https://en.wikipedia.org/wiki/Endianness#Networking) is big-endian — most significant byte leading — so a 16 bit integer holding the value `1` shows up as the two hex bytes `00 01`. Yet the prevalent processors (x86/AMD64, ARM, RISC-V) run little-endian, least significant byte leading, and that same `1` becomes `01 00`.

Socket libraries supply routines for shuffling 16 and 32 bit integers — `ntohl, htonl, ntohs, htons`, in which “n” stands for *network*, “h” for *host*, “s” for *short*, and “l” for *long*. When network order already matches host order these are no-ops, but on a byte-reversed machine they flip the bytes about as needed.

Here in the era of 64-bit machines, spelling binary data out in ASCII often comes out shorter than the binary form itself. The reason is that, surprisingly often, integers carry the value 0, or maybe 1. The string `"0"` runs to two bytes, whereas a full 64-bit integer eats 8. Naturally that sits awkwardly with fixed-length messages. Decisions, decisions.

[Subject index](INDEX.md) · [Previous source context](using-a-socket.md) · [Following source context](disconnecting.md)
