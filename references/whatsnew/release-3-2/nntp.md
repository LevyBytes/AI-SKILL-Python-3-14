# What's New In Python 3.2 / nntp

### nntp

A reworked implementation of the `nntplib` module brings cleaner bytes and text semantics plus more usable APIs. The upside comes at the cost of compatibility with the Python 3.1 nntplib, itself only partly functional.

Secure connections now work too, whether implicit (via `nntplib.NNTP_SSL`) or explicit (via `nntplib.NNTP.starttls()`) TLS.

(Contributed by Antoine Pitrou in [bpo-9360](https://bugs.python.org/issue?@action=redirect&bpo=9360) and Andrew Vant in [bpo-1926](https://bugs.python.org/issue?@action=redirect&bpo=1926).)

[Subject index](INDEX.md) · [Previous source section](ssl.md) · [Next source section](certificates.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
