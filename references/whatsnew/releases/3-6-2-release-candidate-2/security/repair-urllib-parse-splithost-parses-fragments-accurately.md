# Python 3.6.2 release candidate 2 / security / repair urllib parse splithost parses fragments accurately

[bpo-30500](https://bugs.python.org/issue?@action=redirect&bpo=30500): Repair urllib.parse.splithost() so it parses fragments accurately. As an illustration, `splithost('//127.0.0.1#@evil.com/')` from now on correctly returns the `127.0.0.1` host, rather than reading `@evil.com` as the host within an authentication (`login@host`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
