# Python 3.7.0 alpha 1 / library / cgi parse multipart reworked reuse fieldstorage class multipart form data requests output

[bpo-29979](https://bugs.python.org/issue?@action=redirect&bpo=29979): cgi.parse_multipart was reworked to reuse the FieldStorage class so that, for multipart/form-data requests, its output lines up with what FieldStorage yields. Pierre Quentel contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
