# ipaddress: `overlaps()`, `address_exclude()`, `subnets()`, `supernet()`, `subnet_of()`, `supernet_of()`, `compare_networks()`

overlaps(*other*)

 address_exclude(*network*)

 subnets(*prefixlen_diff=1*, *new_prefix=None*)

 supernet(*prefixlen_diff=1*, *new_prefix=None*)

 subnet_of(*other*)

 supernet_of(*other*)

 compare_networks(*other*)

See the matching attribute write-ups under `IPv4Network` for details.

 is_site_local

For the network taken in full, this attribute holds true precisely when it holds true for the network address and the broadcast address alike.

[Subject index](INDEX.md) · [Previous](ipaddress-ipv6network-class-to-ipaddress-ipv6network-hosts.md) · [Continue](operators.md) · [Owning module, declaration or section: ipaddress.IPv6Network](ipaddress-ipv6network-class-to-ipaddress-ipv6network-hosts.md) · [Owning module, declaration or section: Network objects](ipaddress-ipv4network-class.md)
