# Comparisons

### Comparisons

Where it is meaningful to do so, [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) offers a few plain and, one hopes, intuitive means of comparing objects:

```python
>>> ipaddress.ip_address('192.0.2.1') < ipaddress.ip_address('192.0.2.2')
True

```

Should you attempt to compare objects whose versions differ or whose types differ, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception follows.

[Subject index](INDEX.md) · [Previous source context](networks-as-lists-of-addresses.md) · [Following source context](using-ip-addresses-with-other-modules.md)
