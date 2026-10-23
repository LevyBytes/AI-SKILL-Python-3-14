# ssl - Best defaults

### Security considerations

### Best defaults

For **client use**, when you have no particular demands on your security policy, the strong recommendation is to build your SSL context with the `create_default_context()` function. It will pull in the system's trusted CA certificates, switch on certificate validation and hostname checking, and aim to pick reasonably secure protocol and cipher settings.

By way of illustration, here is the way you would employ the [`smtplib.SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) class to set up a trusted, secure connection to a SMTP server:

```python
>>> import ssl, smtplib
>>> smtp = smtplib.SMTP("mail.python.org", port=587)
>>> context = ssl.create_default_context()
>>> smtp.starttls(context=context)
(220, b'2.0.0 Ready to start TLS')

```

Should the connection call for a client certificate, you can attach it with `SSLContext.load_cert_chain()`.

On the other hand, if you build the SSL context by invoking the `SSLContext` constructor on your own, it will arrive with neither certificate validation nor hostname checking turned on by default. If you take that route, please go through the paragraphs that follow to reach a sound security level.

[Subject index](INDEX.md) · [Continue](ssl-manual-certificate-protocol-and-cipher-settings.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
