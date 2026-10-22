# Using IP Addresses with other modules

### Using IP Addresses with other modules

Modules elsewhere that deal in IP addresses (for instance [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket)) generally will not take this module's objects as-is. You instead have to convert them into an integer or a string that the other module is willing to take:

```python
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> str(addr4)
'192.0.2.1'
>>> int(addr4)
3221225985

```

[Subject index](INDEX.md) · [Previous source context](comparisons.md) · [Following source context](getting-more-detail-when-instance-creation-fails.md)
