# ipaddress: `ipaddress.IPv4Interface`

### Interface objects

Because interface objects are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), you can employ them as dictionary keys.

 *class *ipaddress.IPv4Interface(*address*)

Build an IPv4 interface. Here *address* carries the same meaning it has in the `IPv4Network` constructor, the difference being that any host address whatsoever is accepted.

Since `IPv4Interface` derives from `IPv4Address`, every attribute of that parent class carries over to it. On top of those, these further attributes are on offer:

[Subject index](INDEX.md) · [Previous](networks-as-containers-of-addresses.md) · [Continue](interface-objects.md)
