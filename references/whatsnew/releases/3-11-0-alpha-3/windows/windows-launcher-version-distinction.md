# Python 3.11.0 alpha 3 / windows / corrected python launcher can tell versions apart whenever either

[bpo-45616](https://bugs.python.org/issue?@action=redirect&bpo=45616): Corrected the Python Launcher so it can tell versions 3.1 and 3.10 apart whenever either is explicitly asked for. Formerly, if 3.10 was requested yet absent, 3.1 was chosen, and a request for 3.1 yielded 3.10 whenever 3.10 happened to be present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
