# Python 3.7.0 alpha 1 / security / urllib parse splithost fixed parses fragments properly

[bpo-30500](https://bugs.python.org/issue?@action=redirect&bpo=30500): urllib.parse.splithost() was fixed so it parses fragments properly. As an illustration, `splithost('//127.0.0.1#@evil.com/')` now rightly yields the `127.0.0.1` host instead of mistaking `@evil.com` for the host within an authentication (`login@host`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
