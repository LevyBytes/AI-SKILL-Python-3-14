# smtplib: `smtplib.LMTP`

*class *smtplib.LMTP(*host=''*, *port=LMTP_PORT*, *local_hostname=None*, *source_address=None*[, *timeout*])

The LMTP protocol, closely resembling ESMTP, builds heavily on the standard SMTP client. Since Unix sockets are frequently used for LMTP, our `connect()` method has to handle those alongside an ordinary host:port server. The optional arguments *local_hostname* and *source_address* carry the same significance they hold in the `SMTP` class. To name a Unix socket, supply an absolute path for *host* that begins with a ‘/’.

Authentication is available through the usual SMTP mechanism. Over a Unix socket, LMTP typically neither supports nor demands any authentication, though results may differ for you.

Changed in version 3.9: The optional *timeout* parameter was added.

There is also a good assortment of exceptions defined:

[Subject index](INDEX.md) · [Previous](smtplib-smtp-ssl-class.md) · [Continue](smtplib-smtpexception-to-smtplib-smtpauthenticationerror.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md)
