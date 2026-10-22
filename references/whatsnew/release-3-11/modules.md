# What's New In Python 3.11 / Modules

### Modules

- Following [**PEP 594**](https://peps.python.org/pep-0594/), these modules were deprecated and earmarked for removal in Python 3.13:

| `aifc` | `chunk` | `msilib` | `pipes` | `telnetlib` |
| --- | --- | --- | --- | --- |
| `audioop` | `crypt` | `nis` | `sndhdr` | `uu` |
| `cgi` | `imghdr` | `nntplib` | `spwd` | `xdrlib` |
| `cgitb` | `mailcap` | `ossaudiodev` | `sunau` |  |

(Contributed by Brett Cannon in [bpo-47061](https://bugs.python.org/issue?@action=redirect&bpo=47061) and Victor Stinner in [gh-68966](https://github.com/python/cpython/issues/68966).)

- Going back to at least Python 3.6, the `asynchat`, `asyncore` and `smtpd` modules carried a deprecation. Their docs and warnings were refreshed to flag a Python 3.12 removal. (Contributed by Hugo van Kemenade in [bpo-47022](https://bugs.python.org/issue?@action=redirect&bpo=47022).)

- Both the `lib2to3` package and the `2to3` tool are deprecated now and might choke on parsing Python 3.10 or anything newer. For the rationale, look at [**PEP 617**](https://peps.python.org/pep-0617/), which brings in the new PEG parser. (Contributed by Victor Stinner in [bpo-40360](https://bugs.python.org/issue?@action=redirect&bpo=40360).)

- The undocumented `sre_compile`, `sre_constants` and `sre_parse` modules are deprecated as of now. (Contributed by Serhiy Storchaka in [bpo-47152](https://bugs.python.org/issue?@action=redirect&bpo=47152).)

[Subject index](INDEX.md) · [Previous source section](language-builtins.md) · [Next source section](standard-library.md) · [Release/subject declaration](summary-release-highlights.md)
