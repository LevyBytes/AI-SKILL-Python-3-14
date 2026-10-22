# Python 3.7.0 beta 5 / library / functions and types

[bpo-33495](https://bugs.python.org/issue?@action=redirect&bpo=33495): Switch dataclasses.Fields repr so it uses the repr of each member rather than str. This clarifies what every field actually stands for. The benefit is most apparent for the "type" member.

[bpo-33654](https://bugs.python.org/issue?@action=redirect&bpo=33654): Allow protocol type switching within SSLTransport.set_protocol().

[bpo-33652](https://bugs.python.org/issue?@action=redirect&bpo=33652): Pickles produced from type variables plus subscripted generics are now future-proof and interoperable with earlier Python versions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
