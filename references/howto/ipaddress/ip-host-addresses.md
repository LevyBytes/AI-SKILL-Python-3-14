# IP Host Addresses

### IP Host Addresses

Addresses, which people frequently call “host addresses”, form the smallest building block in IP addressing. To make one with the least fuss, lean on the [`ipaddress.ip_address()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.ip_address) factory function; it works out on its own, from whatever value you hand it, whether an IPv4 or IPv6 address should be produced:

```python
>>> ipaddress.ip_address('192.0.2.1')
IPv4Address('192.0.2.1')
>>> ipaddress.ip_address('2001:DB8::1')
IPv6Address('2001:db8::1')

```

You may likewise construct addresses straight from integers. Any value that sits inside 32 bits is taken to be an IPv4 address:

```python
>>> ipaddress.ip_address(3221225985)
IPv4Address('192.0.2.1')
>>> ipaddress.ip_address(42540766411282592856903984951653826561)
IPv6Address('2001:db8::1')

```

When you want to insist on IPv4 or IPv6 addresses, call the corresponding classes outright. That approach really shines when you need small integers turned into IPv6 addresses:

```python
>>> ipaddress.ip_address(1)
IPv4Address('0.0.0.1')
>>> ipaddress.IPv4Address(1)
IPv4Address('0.0.0.1')
>>> ipaddress.IPv6Address(1)
IPv6Address('::1')

```

[Subject index](INDEX.md) · [Previous source context](a-note-on-ip-versions.md) · [Following source context](defining-networks.md)
