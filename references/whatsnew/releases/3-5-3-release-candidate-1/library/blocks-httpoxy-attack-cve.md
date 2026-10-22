# Python 3.5.3 release candidate 1 / library / blocks httpoxy attack cve

[bpo-27568](https://bugs.python.org/issue?@action=redirect&bpo=27568): Blocks the HTTPoxy attack ([**CVE 2016-1000110**](https://www.cve.org/CVERecord?id=CVE-2016-1000110)). The HTTP_PROXY variable is disregarded whenever the REQUEST_METHOD environment variable is present, a sign that the script runs in CGI mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
