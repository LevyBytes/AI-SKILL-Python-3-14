# Python 3.10 changes: Removed compiler helpers and tracing internals

Carrying no documentation, these functions sat outside the limited C API and served purely as internal helpers for the compiler. (Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- In the interest of speeding Python up, the `PyThreadState.use_tracing` member is gone. (Contributed by Mark Shannon in [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760).)

[Subject index](INDEX.md) · [Next source section](notable-security-feature-in-3-10-7.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md) · [Release/subject declaration](c-api-changes-removed-removed.md) · [Preceding release/subject continuation](c-api-changes-removed-py-symtablestringobject.md)
