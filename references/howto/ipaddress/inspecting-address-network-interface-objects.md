# Inspecting Address/Network/Interface Objects

### Inspecting Address/Network/Interface Objects

Having put in the effort to build an IPv(4|6)(Address|Network|Interface) object, you will most likely want to pull details out of it. [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) aims to keep that straightforward and natural.

Extracting the IP version:

```python
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> addr6 = ipaddress.ip_address('2001:db8::1')
>>> addr6.version
6
>>> addr4.version
4

```

Pulling the network out of an interface:

```python
>>> host4 = ipaddress.ip_interface('192.0.2.1/24')
>>> host4.network
IPv4Network('192.0.2.0/24')
>>> host6 = ipaddress.ip_interface('2001:db8::1/96')
>>> host6.network
IPv6Network('2001:db8::/96')

```

Counting the individual addresses that a network holds:

```python
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> net4.num_addresses
256
>>> net6 = ipaddress.ip_network('2001:db8::0/96')
>>> net6.num_addresses
4294967296

```

Walking across a network's “usable” addresses:

```python
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> for x in net4.hosts():
...     print(x)
192.0.2.1
192.0.2.2
192.0.2.3
192.0.2.4
...
192.0.2.252
192.0.2.253
192.0.2.254

```

Fetching the netmask (that is, the bits set to match the network prefix) or else the hostmask (whatever bits lie outside the netmask):

```python
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> net4.netmask
IPv4Address('255.255.255.0')
>>> net4.hostmask
IPv4Address('0.0.0.255')
>>> net6 = ipaddress.ip_network('2001:db8::0/96')
>>> net6.netmask
IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff::')
>>> net6.hostmask
IPv6Address('::ffff:ffff')

```

Exploding or compressing the address:

```python
>>> addr6.exploded
'2001:0db8:0000:0000:0000:0000:0000:0001'
>>> addr6.compressed
'2001:db8::1'
>>> net6.exploded
'2001:0db8:0000:0000:0000:0000:0000:0000/96'
>>> net6.compressed
'2001:db8::/96'

```

Even though IPv4 has no notion of explosion or compression, its objects nonetheless expose the matching properties, which lets version-neutral code readily settle on the tightest or fullest form for IPv6 addresses and go on handling IPv4 addresses properly all the while.

[Subject index](INDEX.md) · [Previous source context](host-interfaces.md) · [Following source context](networks-as-lists-of-addresses.md)
