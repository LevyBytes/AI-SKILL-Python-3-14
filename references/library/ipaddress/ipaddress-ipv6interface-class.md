# ipaddress: `ipaddress.IPv6Interface`

*class *ipaddress.IPv6Interface(*address*)

Build an IPv6 interface. Here *address* carries the same meaning it has in the `IPv6Network` constructor, the difference being that any host address whatsoever is accepted.

Since `IPv6Interface` derives from `IPv6Address`, every attribute of that parent class carries over to it. On top of those, these further attributes are on offer:

 ip

 network

 with_prefixlen

 with_netmask

 with_hostmask

Consult the matching attribute write-ups under `IPv4Interface`.

[Subject index](INDEX.md) · [Previous](interface-objects.md) · [Continue](operators.md) · [Owning module, declaration or section: Interface objects](ipaddress-ipv4interface-class.md)
