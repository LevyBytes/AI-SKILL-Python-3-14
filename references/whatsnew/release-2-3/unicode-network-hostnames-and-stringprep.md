# What’s New in Python 2.3 / New, Improved, and Deprecated Modules - ftplib, socket, stringprep, urllib

The [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module has likewise been broadened to seamlessly translate Unicode hostnames into the ACE form before forwarding them to the C library. Modules handling hostnames, including `httplib` and [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib)), accept Unicode host names too; `httplib` additionally transmits HTTP `Host` headers using the ACE form of the domain name. [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib) handles Unicode URLs carrying non-ASCII host names provided that the `path` portion of the URL stays ASCII only.

Delivering this change required adding the [`stringprep`](https://docs.python.org/3.14/library/stringprep.html#module-stringprep) module, the `mkstringprep` tool, and the `punycode` encoding.

[Subject index](INDEX.md) · [Previous source section](tkinter-shelve-and-dom-compatibility.md) · [Next source section](date-time-type.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](text-threading-and-timing-updates.md)
