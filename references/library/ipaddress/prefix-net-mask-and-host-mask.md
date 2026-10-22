# Prefix, net mask and host mask

### Prefix, net mask and host mask

IP network masks can be expressed in several interchangeable ways. A *prefix* `/<nbits>` is notation stating how many high-order bits the network mask sets. A *net mask* is an IP address with a certain count of high-order bits set. So the prefix `/24` matches the net mask `255.255.255.0` in IPv4, or `ffff:ff00::` in IPv6. On top of that, a *host mask* is the logical complement of a *net mask*, and sometimes serves (for instance in Cisco access control lists) to express a network mask. In IPv4, the host mask matching `/24` is `0.0.0.255`.

[Subject index](INDEX.md) · [Previous](ip-network-definitions.md) · [Continue](ipaddress-ipv4network-class.md)
