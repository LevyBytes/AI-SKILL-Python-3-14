# ipaddress: IP interface address, network and notation properties

ip

The bare address (`IPv4Address`), stripped of any network information.

```python
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.ip
IPv4Address('192.0.2.5')

```

 network

The network (`IPv4Network`) to which this interface is attached.

```python
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.network
IPv4Network('192.0.2.0/24')

```

 with_prefixlen

A string form of the interface in which the mask appears using prefix notation.

```python
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_prefixlen
'192.0.2.5/24'

```

 with_netmask

A string form of the interface in which the network is shown as a net mask.

```python
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_netmask
'192.0.2.5/255.255.255.0'

```

 with_hostmask

A string form of the interface in which the network is shown as a host mask.

```python
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_hostmask
'192.0.2.5/0.0.0.255'

```

[Subject index](INDEX.md) · [Previous](ipaddress-ipv4interface-class.md) · [Continue](ipaddress-ipv6interface-class.md) · [Owning module, declaration or section: ipaddress.IPv4Interface](ipaddress-ipv4interface-class.md) · [Owning module, declaration or section: Interface objects](ipaddress-ipv4interface-class.md)
