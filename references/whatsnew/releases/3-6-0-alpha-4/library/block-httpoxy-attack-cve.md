# Python 3.6.0 alpha 4 / library / block httpoxy attack cve

[bpo-27568](https://bugs.python.org/issue?@action=redirect&bpo=27568): Block the HTTPoxy attack ([**CVE 2016-1000110**](https://www.cve.org/CVERecord?id=CVE-2016-1000110)). When the REQUEST_METHOD environment is present — signalling CGI mode for the script — disregard the HTTP_PROXY variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
