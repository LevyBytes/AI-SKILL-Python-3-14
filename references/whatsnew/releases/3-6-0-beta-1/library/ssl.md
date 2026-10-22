# Python 3.6.0 beta 1 / library / ssl

[bpo-27850](https://bugs.python.org/issue?@action=redirect&bpo=27850): Drop 3DES from the ssl module's default cipher list as a countermeasure against the sweet32 attack ([**CVE 2016-2183**](https://www.cve.org/CVERecord?id=CVE-2016-2183)).

[bpo-27766](https://bugs.python.org/issue?@action=redirect&bpo=27766): ChaCha20 Poly1305 was added to the ssl module's default cipher list. (Needed OpenSSL 1.1.0 or LibreSSL).

[bpo-27691](https://bugs.python.org/issue?@action=redirect&bpo=27691): Correct how the ssl module parses GEN_RID subject alternative name fields inside X.509 certs.

[bpo-28025](https://bugs.python.org/issue?@action=redirect&bpo=28025): Turn every ssl module constant into IntEnum and IntFlags. SSLContext properties hand back flags and enums now.

[bpo-19500](https://bugs.python.org/issue?@action=redirect&bpo=19500): Give the ssl module client-side SSL session resumption.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
