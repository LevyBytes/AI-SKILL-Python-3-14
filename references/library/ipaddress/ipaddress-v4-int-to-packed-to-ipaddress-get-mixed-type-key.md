# Other Module Level Functions

### Other Module Level Functions

Beyond those, the module exposes the module level functions listed here:

 ipaddress.v4_int_to_packed(*address*)

Render an address as 4 packed bytes laid out in network (big-endian) order. The *address* argument is an integer rendering of an IPv4 IP address. Where that integer is negative, or too large to count as an IPv4 IP address, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

```python
>>> ipaddress.ip_address(3221225985)
IPv4Address('192.0.2.1')
>>> ipaddress.v4_int_to_packed(3221225985)
b'\xc0\x00\x02\x01'

```

 ipaddress.v6_int_to_packed(*address*)

Render an address as 16 packed bytes laid out in network (big-endian) order. The *address* argument is an integer rendering of an IPv6 IP address. Where that integer is negative, or too large to count as an IPv6 IP address, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

 ipaddress.summarize_address_range(*first*, *last*)

Hand back an iterator over the summarized network range derived from the first and last IP addresses. *first* marks the opening `IPv4Address` or `IPv6Address` of the range, and *last* marks the closing `IPv4Address` or `IPv6Address`. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results when *first* or *last* are not IP addresses, or do not share the same version. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results when *last* fails to exceed *first*, or when the *first* address version is neither 4 nor 6.

```python
>>> [ipaddr for ipaddr in ipaddress.summarize_address_range(
...    ipaddress.IPv4Address('192.0.2.0'),
...    ipaddress.IPv4Address('192.0.2.130'))]
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'), IPv4Network('192.0.2.130/32')]

```

 ipaddress.collapse_addresses(*addresses*)

Hand back an iterator over the collapsed `IPv4Network` or `IPv6Network` objects. The *addresses* argument is an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of `IPv4Network` or `IPv6Network` objects. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results whenever *addresses* mixes objects of differing versions.

```python
>>> [ipaddr for ipaddr in
... ipaddress.collapse_addresses([ipaddress.IPv4Network('192.0.2.0/25'),
... ipaddress.IPv4Network('192.0.2.128/25')])]
[IPv4Network('192.0.2.0/24')]

```

 ipaddress.get_mixed_type_key(*obj*)

Hand back a key fit for sorting across a mixture of networks and addresses. Out of the box, Address and Network objects cannot be sorted together, since they differ at a fundamental level, which is why the expression:

```python
IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

```

carries no meaning. On occasion, though, you might still want `ipaddress` to sort such a mix. When that need arises, pass this function along as the *key* argument to [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted).

The *obj* argument is one of the two: a network object or an address object.

[Subject index](INDEX.md) · [Previous](logical-operators.md) · [Continue](ipaddress-addressvalueerror-to-ipaddress-netmaskvalueerror.md)
