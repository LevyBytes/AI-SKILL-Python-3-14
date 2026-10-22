# What’s New In Python 3.5 / email — email.policy

### email

A fresh policy option [`Policy.mangle_from_`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.mangle_from_) decides whether generators prefix a `">"` character onto lines within email bodies that open with `"From "`. The default sits at `True` for [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) while staying `False` across every other policy. (Contributed by Milan Oberkirch in [bpo-20098](https://bugs.python.org/issue?@action=redirect&bpo=20098).)

To make the *Content-Disposition* header's canonical value easy to retrieve, the method [`Message.get_content_disposition()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_content_disposition) was added. (Contributed by Abhilash Raj in [bpo-21083](https://bugs.python.org/issue?@action=redirect&bpo=21083).)

By setting the fresh policy option [`EmailPolicy.utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) to `True`, email headers are encoded with the UTF-8 charset rather than relying on encoded words. With this, `Messages` can follow the formatting of [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html) and work alongside an SMTP server that offers the [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html) `SMTPUTF8` extension. (Contributed by R. David Murray in [bpo-24211](https://bugs.python.org/issue?@action=redirect&bpo=24211).)

A [`charset.Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance may now be supplied to the [`mime.text.MIMEText`](https://docs.python.org/3.14/library/email.mime.html#email.mime.text.MIMEText) constructor. (Contributed by Claude Paroz and Berker Peksag in [bpo-16324](https://bugs.python.org/issue?@action=redirect&bpo=16324).)

[Subject index](INDEX.md) · [Previous source section](doctest.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](enum.md)
