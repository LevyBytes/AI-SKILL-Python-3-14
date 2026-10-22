# Iteration

#### Iteration

Iterating a network object walks through every address that the network contains. During iteration *all* hosts come back, the unusable ones included (when you want only usable hosts, reach for the `hosts()` method). For example:

```python
>>> for addr in IPv4Network('192.0.2.0/28'):
...     addr
...
IPv4Address('192.0.2.0')
IPv4Address('192.0.2.1')
IPv4Address('192.0.2.2')
IPv4Address('192.0.2.3')
IPv4Address('192.0.2.4')
IPv4Address('192.0.2.5')
IPv4Address('192.0.2.6')
IPv4Address('192.0.2.7')
IPv4Address('192.0.2.8')
IPv4Address('192.0.2.9')
IPv4Address('192.0.2.10')
IPv4Address('192.0.2.11')
IPv4Address('192.0.2.12')
IPv4Address('192.0.2.13')
IPv4Address('192.0.2.14')
IPv4Address('192.0.2.15')

```

[Subject index](INDEX.md) · [Previous](logical-operators.md) · [Continue](networks-as-containers-of-addresses.md)
