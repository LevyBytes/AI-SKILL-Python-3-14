# encodings.idna — `encodings.idna` — Internationalized Domain Names in Applications

### `encodings.idna` — Internationalized Domain Names in Applications

What this module provides is [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html) (Internationalized Domain Names in Applications) together with [**RFC 3492**](https://datatracker.ietf.org/doc/html/rfc3492.html) (Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)). Its foundation is the `punycode` encoding plus [`stringprep`](https://docs.python.org/3.14/library/stringprep.html#module-stringprep).

Where the IDNA 2008 standard laid out in [**RFC 5891**](https://datatracker.ietf.org/doc/html/rfc5891.html) and [**RFC 5895**](https://datatracker.ietf.org/doc/html/rfc5895.html) is what you require, turn to the third-party [idna](https://pypi.org/project/idna/) module.

Taken together these RFCs spell out a protocol for letting non-ASCII characters appear in domain names. Any domain name carrying non-ASCII characters (for instance `www.Alliancefrançaise.nu`) gets turned into an ASCII-compatible encoding (ACE, for instance `www.xn--alliancefranaise-npb.nu`). That ACE rendering of the domain name then serves everywhere the protocol forbids arbitrary characters — DNS queries, HTTP *Host* fields, and the like. The application is where this conversion happens, ideally without the user ever noticing: domain labels in Unicode should be quietly turned into IDNA going out on the wire, and ACE labels turned back into Unicode before they reach the user.

Several avenues for this conversion exist in Python: the `idna` codec moves data both ways between Unicode and ACE, breaking an input string into labels according to the separator characters laid out in [**section 3.1 of RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html#section-3.1) and turning each label into ACE when needed, while in reverse it splits an input byte string into labels at the `.` separator and turns any ACE labels it spots into unicode. Beyond that, the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module quietly converts Unicode host names into ACE, sparing applications from having to convert host names on their own before handing them to the socket module. Additionally, modules taking host names as function parameters — [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) and [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) among them — will accept Unicode host names (`http.client` will, where it sends the *Host* field at all, also slip an IDNA hostname into it without fuss).

Host names arriving off the wire (as happens in reverse name lookup) undergo no automatic conversion to Unicode: an application that intends to show such host names to the user ought to decode them into Unicode itself.

On top of that, the `encodings.idna` module carries out the nameprep procedure, which applies particular normalizations to host names so that international domain names become case-insensitive and lookalike characters get folded together. Should you want them, the nameprep functions are callable on their own.

 encodings.idna.nameprep(*label*)

Give back *label* once it has been nameprepped. As things stand, the implementation presumes query strings, hence `AllowUnassigned` holds true.

 encodings.idna.ToASCII(*label*)

Turn a label into ASCII, following what [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html) lays out. The presumption is that `UseSTD3ASCIIRules` is false.

 encodings.idna.ToUnicode(*label*)

Turn a label into Unicode, following what [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html) lays out.

[Subject index](INDEX.md) · [Previous](../encodings/encodings-normalize-encoding-to-encodings-codecregistryerror.md) · [Continue](../encodings-mbcs/encodings-mbcs-windows-ansi-codepage.md)
