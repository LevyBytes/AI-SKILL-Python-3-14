# What’s New in Python 2.7 / PEP 466: Network Security Enhancements for Python 2.7 - hashlib, hmac, os, ssl

[**PEP 466**](https://peps.python.org/pep-0466/) lays out several proposed network-security improvements that have been cleared to ship in the Python 2.7 maintenance line, and the earliest of those changes landed in the Python 2.7.7 release.

[**PEP 466**](https://peps.python.org/pep-0466/) related features added in Python 2.7.7:

- [`hmac.compare_digest()`](https://docs.python.org/3.14/library/hmac.html#hmac.compare_digest) came over from Python 3 by backport, giving Python 2 programs access to a comparison routine that resists timing attacks. (Contributed by Alex Gaynor; [bpo-21306](https://bugs.python.org/issue?@action=redirect&bpo=21306).)

- The official Windows installers distributed on python.org moved up to OpenSSL 1.0.1g. (Contributed by Zachary Ware; [bpo-21462](https://bugs.python.org/issue?@action=redirect&bpo=21462).)

[**PEP 466**](https://peps.python.org/pep-0466/) related features added in Python 2.7.8:

- [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac) was carried back from Python 3 so that a hashing scheme fit for safe password storage would be widely reachable by Python 2 programs. (Contributed by Alex Gaynor; [bpo-21304](https://bugs.python.org/issue?@action=redirect&bpo=21304).)

- For the official Windows installers on python.org, OpenSSL was bumped to 1.0.1h. (Contributed by Zachary Ware in [bpo-21671](https://bugs.python.org/issue?@action=redirect&bpo=21671) for [**CVE 2014-0224**](https://www.cve.org/CVERecord?id=CVE-2014-0224).)

[**PEP 466**](https://peps.python.org/pep-0466/) related features added in Python 2.7.9:

- The bulk of the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module from Python 3.4 was brought back. As a result, `ssl` now handles Server Name Indication, TLS1.x configuration, reaching the platform certificate store, the [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) class, and more besides. (Contributed by Alex Gaynor and David Reid; [bpo-21308](https://bugs.python.org/issue?@action=redirect&bpo=21308).)

Consult the “Version added: 2.7.9” remarks in the module's documentation for the precise particulars.

- [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) was adjusted so it now holds onto a cached file descriptor for `/dev/urandom` rather than opening `/dev/urandom` afresh at each call. (Contributed by Alex Gaynor; [bpo-21305](https://bugs.python.org/issue?@action=redirect&bpo=21305).)

- [`hashlib.algorithms_guaranteed`](https://docs.python.org/3.14/library/hashlib.html#hashlib.algorithms_guaranteed) and [`hashlib.algorithms_available`](https://docs.python.org/3.14/library/hashlib.html#hashlib.algorithms_available) were ported back from Python 3, simplifying the job of picking the strongest hash algorithm on offer for Python 2 programs. (Contributed by Alex Gaynor in [bpo-21307](https://bugs.python.org/issue?@action=redirect&bpo=21307))

[Subject index](INDEX.md) · [Next source section](pep-477-backport-ensurepip-to-python-2-7.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](pep-434-idle-enhancement-exception-for-all-branches.md) · [Preceding release/subject continuation](pep-434-idle-enhancement-exception-for-all-branches.md)
