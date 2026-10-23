# ssl - CA certificates

### CA certificates

Should you intend to demand validation of the certificate from the connection's other end, you must supply a "CA certs" file populated with the certificate chains for every issuer you choose to trust. Once more, this file merely holds those chains concatenated one after another. During validation, Python selects the first chain in the file that produces a match. You can employ the platform's certificates file by invoking `SSLContext.load_default_certs()`; `create_default_context()` performs this for you automatically.

[Subject index](INDEX.md) · [Previous](certificate-chains.md) · [Continue](combined-key-and-certificate.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
