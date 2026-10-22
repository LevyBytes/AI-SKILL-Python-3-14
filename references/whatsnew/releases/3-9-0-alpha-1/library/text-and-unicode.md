# Python 3.9.0 alpha 1 / library / text and unicode

[bpo-37587](https://bugs.python.org/issue?@action=redirect&bpo=37587): Sped up json.loads for lengthy strings. (Marco Paolini wrote the patch)

[bpo-18378](https://bugs.python.org/issue?@action=redirect&bpo=18378): Treat ?UTF-8? as an acceptable LC_CTYPE value within locale._parse_localename.

[bpo-37405](https://bugs.python.org/issue?@action=redirect&bpo=37405): A regression in socket.getsockname() affecting non-CAN_ISOTP AF_CAN address family sockets was fixed by returning a 1-tuple in place of a string.

[bpo-37111](https://bugs.python.org/issue?@action=redirect&bpo=37111): `logging.basicConfig` picked up `encoding` and `errors` keyword parameters.

[bpo-37723](https://bugs.python.org/issue?@action=redirect&bpo=37723): Addressed a slowdown when regular expressions parse very large character sets. Yann Vaginay wrote the patch.

[bpo-13153](https://bugs.python.org/issue?@action=redirect&bpo=13153): Conversion between Python strings and Tcl objects now relies on the OS native encoding. As a result, emoji and other characters outside the BMP can be shown, copied, and pasted to the clipboard. The round trip from Tcl to Python and back is now guaranteed never to fail (the lone exception being MemoryError).

[bpo-32820](https://bugs.python.org/issue?@action=redirect&bpo=32820): `__format__` was added to the IPv4 and IPv6 classes. The result is always a fully zero-padded string. The b/x/n modifiers (bin/hex/native format) are supported; native format for IPv4 is bin, while native format for IPv6 is hex. The "#" and "_" modifiers are honored as well.

[bpo-37587](https://bugs.python.org/issue?@action=redirect&bpo=37587): `_json.scanstring` now runs as much as 3x faster whenever the JSON string holds numerous backslash escaped characters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
