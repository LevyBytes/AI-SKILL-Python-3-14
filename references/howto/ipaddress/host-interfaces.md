# Host Interfaces

### Host Interfaces

As noted a moment ago, when you have to pin down an address on a specific network, neither the address classes nor the network classes will do on their own. Network engineers, along with those who craft tooling for firewalls and routers, lean on notation like `192.0.2.1/24` as a shorthand meaning “the host `192.0.2.1` on the network `192.0.2.0/24`”, Accordingly, [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) furnishes a family of hybrid classes that bind an address to a specific network. Creating one follows the very same interface as defining network objects, save that the address portion is no longer required to be a network address.

```python
>>> ipaddress.ip_interface('192.0.2.1/24')
IPv4Interface('192.0.2.1/24')
>>> ipaddress.ip_interface('2001:db8::1/96')
IPv6Interface('2001:db8::1/96')

```

Integer inputs work here as well (the same as with networks), and you can compel a given IP version by calling the appropriate constructor outright.

[Subject index](INDEX.md) · [Previous source context](defining-networks.md) · [Following source context](inspecting-address-network-interface-objects.md)
