# Python 3.9.0 alpha 6 / core and builtins / development

[bpo-37388](https://bugs.python.org/issue?@action=redirect&bpo=37388): During Python finalization, str.encode() and str.decode() no longer validate the encoding and errors under development mode or debug mode. On extremely late str.encode() and str.decode() calls, the codecs machinery cannot operate anymore.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
