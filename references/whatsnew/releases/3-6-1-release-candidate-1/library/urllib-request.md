# Python 3.6.1 release candidate 1 / library / urllib request

[bpo-29142](https://bugs.python.org/issue?@action=redirect&bpo=29142): Within urllib.request, suffixes carried in the no_proxy environment variable using leading dots could once more match related hostnames (for instance, .b.c matches a.b.c). Milan Oberkirch wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
