# What's New In Python 3.4 / smtpd

### smtpd

The `SMTPServer` and `SMTPChannel` classes now take a *map* keyword argument; when given, that value is forwarded to `asynchat.async_chat` as its *map* argument. By doing so, a program can keep from disturbing the global socket map. (Contributed by Vinay Sajip in [bpo-11959](https://bugs.python.org/issue?@action=redirect&bpo=11959).)

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](smtplib.md) · [Release/subject declaration](release-highlights.md)
