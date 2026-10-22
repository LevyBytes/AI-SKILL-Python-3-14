# Networks as containers of addresses

#### Networks as containers of addresses

A network object is able to serve as a container holding addresses. A few illustrations:

```python
>>> IPv4Network('192.0.2.0/28')[0]
IPv4Address('192.0.2.0')
>>> IPv4Network('192.0.2.0/28')[15]
IPv4Address('192.0.2.15')
>>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
True
>>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
False

```

[Subject index](INDEX.md) · [Previous](iteration.md) · [Continue](ipaddress-ipv4interface-class.md)
