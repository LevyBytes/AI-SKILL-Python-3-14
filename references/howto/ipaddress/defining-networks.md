# Defining Networks

### Defining Networks

Host addresses tend to be gathered into IP networks, and so [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) gives you the means to build, examine and adjust network definitions. An IP network object is put together from a string that spells out which range of host addresses the network covers. The plainest way to express that is a “network address/network prefix” pair: the prefix says how many leading bits get checked when deciding whether an address falls inside the network, while the network address fixes what value those bits are expected to hold.

Just as with addresses, there is a factory function that picks the right IP version for you on its own:

```python
>>> ipaddress.ip_network('192.0.2.0/24')
IPv4Network('192.0.2.0/24')
>>> ipaddress.ip_network('2001:db8::0/96')
IPv6Network('2001:db8::/96')

```

A network object is forbidden from carrying any host bits. In practice this means `192.0.2.1/24` fails to denote a network. Definitions of that kind go by the name interface objects, because the ip-on-a-network notation is routinely used to denote a computer's network interfaces on some given network; the section that follows covers them more fully.

Out of the box, trying to build a network object that has host bits set raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). If you would rather have those extra bits forced down to zero, hand the `strict=False` flag to the constructor:

```python
>>> ipaddress.ip_network('192.0.2.1/24')
Traceback (most recent call last):
   ...
ValueError: 192.0.2.1/24 has host bits set
>>> ipaddress.ip_network('192.0.2.1/24', strict=False)
IPv4Network('192.0.2.0/24')

```

Although the string form is far more flexible, you can equally define networks with integers, much as you do host addresses. When you go this route, the network is taken to hold only the lone address that the integer names, so the network prefix spans the whole network address:

```python
>>> ipaddress.ip_network(3221225984)
IPv4Network('192.0.2.0/32')
>>> ipaddress.ip_network(42540766411282592856903984951653826560)
IPv6Network('2001:db8::/128')

```

Here too, as with addresses, you can pin down a specific kind of network by invoking the class constructor outright rather than going through the factory function.

[Subject index](INDEX.md) · [Previous source context](ip-host-addresses.md) · [Following source context](host-interfaces.md)
