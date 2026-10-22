# Python 3.5.4 release candidate 1 / security / tests and documentation

[bpo-30500](https://bugs.python.org/issue?@action=redirect&bpo=30500): Make urllib.parse.splithost() parse fragments correctly. As an example, `splithost('//127.0.0.1#@evil.com/')` now properly yields the `127.0.0.1` host rather than reading `@evil.com` as the host in an authentication (`login@host`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
