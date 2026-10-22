# ssl — Testing for SSL support

### Examples

### Testing for SSL support

If user code wants to check whether a Python installation has SSL support present, the following idiom should be used:

```python
try:
    import ssl
except ImportError:
    pass
else:
    ...  # do something that requires SSL support

```

[Subject index](INDEX.md) · [Continue](tls-client-operation-overview.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
