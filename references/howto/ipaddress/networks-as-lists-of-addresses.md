# Networks as lists of Addresses

### Networks as lists of Addresses

Now and then it pays to handle networks as if they were lists. That, in turn, lets you index into them this way:

```python
>>> net4[1]
IPv4Address('192.0.2.1')
>>> net4[-1]
IPv4Address('192.0.2.255')
>>> net6[1]
IPv6Address('2001:db8::1')
>>> net6[-1]
IPv6Address('2001:db8::ffff:ffff')

```

It also means a network object readily supports the list membership test syntax, as shown here:

```python
if address in network:
    # do something

```

Membership checks run efficiently by leaning on the network prefix:

```python
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> addr4 in ipaddress.ip_network('192.0.2.0/24')
True
>>> addr4 in ipaddress.ip_network('192.0.3.0/24')
False

```

[Subject index](INDEX.md) · [Previous source context](inspecting-address-network-interface-objects.md) · [Following source context](comparisons.md)
