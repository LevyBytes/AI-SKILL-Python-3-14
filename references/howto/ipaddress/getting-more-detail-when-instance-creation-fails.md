# Getting more detail when instance creation fails

### Getting more detail when instance creation fails

If you build address/network/interface objects through the version-agnostic factory functions, whatever goes wrong surfaces as a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) bearing a generic message that merely notes the supplied value was not taken to be an object of that type. No more specific error appears because pinning down the reason for rejection requires knowing whether the value was *supposed* to be IPv4 or IPv6 in the first place.

For situations where getting at that extra detail proves handy, the separate class constructors do in fact raise the [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) subclasses [`ipaddress.AddressValueError`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.AddressValueError) and [`ipaddress.NetmaskValueError`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.NetmaskValueError), pointing precisely at the portion of the definition that would not parse.

Invoke the class constructors outright and the error messages grow far more detailed. To illustrate:

```python
>>> ipaddress.ip_address("192.168.0.256")
Traceback (most recent call last):
  ...
ValueError: '192.168.0.256' does not appear to be an IPv4 or IPv6 address
>>> ipaddress.IPv4Address("192.168.0.256")
Traceback (most recent call last):
  ...
ipaddress.AddressValueError: Octet 256 (> 255) not permitted in '192.168.0.256'

>>> ipaddress.ip_network("192.168.0.1/64")
Traceback (most recent call last):
  ...
ValueError: '192.168.0.1/64' does not appear to be an IPv4 or IPv6 network
>>> ipaddress.IPv4Network("192.168.0.1/64")
Traceback (most recent call last):
  ...
ipaddress.NetmaskValueError: '64' is not a valid netmask

```

That said, since both of these module-specific exceptions descend from [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) as their parent class, whenever the exact error type is of no concern to you, code along these lines remains perfectly workable:

```python
try:
    network = ipaddress.IPv4Network(address)
except ValueError:
    print('address/netmask is invalid for IPv4:', address)

```

[Subject index](INDEX.md) · [Previous source context](using-ip-addresses-with-other-modules.md)
