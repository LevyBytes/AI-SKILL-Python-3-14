# Comparison operators

#### Comparison operators

The familiar collection of comparison operators works on address objects. Identical IPv6 addresses carrying different scope zone IDs do not compare equal. A few examples:

```python
>>> IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
True
>>> IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
False
>>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
True
>>> IPv6Address('fe80::1234') == IPv6Address('fe80::1234%1')
False
>>> IPv6Address('fe80::1234%1') != IPv6Address('fe80::1234%2')
True

```

[Subject index](INDEX.md) · [Previous](operators.md) · [Continue](arithmetic-operators.md)
