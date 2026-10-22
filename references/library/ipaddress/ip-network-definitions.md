# IP Network definitions

### IP Network definitions

The `IPv4Network` and `IPv6Network` objects give you a way to declare and examine IP network definitions. Such a definition is built from a *mask* together with a *network address*, and thereby marks out a span of IP addresses that match the network address once masked (binary AND) against the mask. To illustrate, a definition pairing the mask `255.255.255.0` with the network address `192.168.1.0` covers the IP addresses across the inclusive span `192.168.1.0` to `192.168.1.255`.

[Subject index](INDEX.md) · [Previous](arithmetic-operators.md) · [Continue](prefix-net-mask-and-host-mask.md)
