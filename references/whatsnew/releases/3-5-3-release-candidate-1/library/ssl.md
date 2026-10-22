# Python 3.5.3 release candidate 1 / library / ssl

[bpo-27691](https://bugs.python.org/issue?@action=redirect&bpo=27691): Corrected how the ssl module parses GEN_RID subject alternative name entries inside X.509 certs.

[bpo-27850](https://bugs.python.org/issue?@action=redirect&bpo=27850): Dropped 3DES from the ssl module's default cipher list as a countermeasure against the sweet32 attack ([**CVE 2016-2183**](https://www.cve.org/CVERecord?id=CVE-2016-2183)).

[bpo-27766](https://bugs.python.org/issue?@action=redirect&bpo=27766): Added ChaCha20 Poly1305 into the ssl module's default cipher list. (Needs OpenSSL 1.1.0 or LibreSSL).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
