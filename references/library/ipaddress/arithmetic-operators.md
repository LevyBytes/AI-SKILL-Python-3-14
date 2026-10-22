# Arithmetic operators

#### Arithmetic operators

You can add integers to address objects or subtract integers from them. A few examples:

```python
>>> IPv4Address('127.0.0.2') + 3
IPv4Address('127.0.0.5')
>>> IPv4Address('127.0.0.2') - 3
IPv4Address('126.255.255.255')
>>> IPv4Address('255.255.255.255') + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ipaddress.AddressValueError: 4294967296 (>= 2**32) is not permitted as an IPv4 address

```

[Subject index](INDEX.md) · [Previous](comparison-operators.md) · [Continue](ip-network-definitions.md)
