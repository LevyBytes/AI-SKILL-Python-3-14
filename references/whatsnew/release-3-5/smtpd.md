# What’s New In Python 3.5 / smtpd

### smtpd

A *decode_data* keyword argument is now accepted by both the `SMTPServer` and `SMTPChannel` classes; it controls whether the `DATA` segment of the SMTP transaction gets decoded with the `"utf-8"` codec or is instead handed to the `SMTPServer.process_message()` method as a byte string. For backward-compatibility purposes the default remains `True`, though Python 3.6 will flip it to `False`. Should *decode_data* be `False`, the `process_message` method has to be ready to take keyword arguments. Maciej Szulik contributed this (see [bpo-19662](https://bugs.python.org/issue?@action=redirect&bpo=19662)).

When *decode_data* has been left at `True`, the `SMTPServer` class now announces the `8BITMIME` extension ([**RFC 6152**](https://datatracker.ietf.org/doc/html/rfc6152.html)). Should the client send `BODY=8BITMIME` along with the `MAIL` command, that value reaches `SMTPServer.process_message()` through the *mail_options* keyword. Milan Oberkirch and R. David Murray landed this (see [bpo-21795](https://bugs.python.org/issue?@action=redirect&bpo=21795)).

The `SMTPUTF8` extension ([**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html): Internationalized Email) is now handled by the `SMTPServer` class too. Whenever the client sends `SMTPUTF8 BODY=8BITMIME` with the `MAIL` command, those values flow to `SMTPServer.process_message()` by way of the *mail_options* keyword. Properly dealing with the `SMTPUTF8` data falls to the `process_message` method. Milan Oberkirch contributed this (see [bpo-21725](https://bugs.python.org/issue?@action=redirect&bpo=21725)).

IPv6 addresses — supplied straight or resolved by name — may now be passed to the `SMTPServer` constructor, which will connect with them successfully. Milan Oberkirch added this (see [bpo-14758](https://bugs.python.org/issue?@action=redirect&bpo=14758)).

[Subject index](INDEX.md) · [Previous source section](signal.md) · [Next source section](smtplib.md) · [Release/subject declaration](summary-release-highlights.md)
