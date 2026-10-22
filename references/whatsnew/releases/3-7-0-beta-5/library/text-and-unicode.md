# Python 3.7.0 beta 5 / library / text and unicode

[bpo-33497](https://bugs.python.org/issue?@action=redirect&bpo=33497): Add an errors param to cgi.parse_multipart and let an encoding inside FieldStorage honor the supplied errors (required by Twisted). Patch by Amber Brown.

[bpo-30877](https://bugs.python.org/issue?@action=redirect&bpo=30877): Repaired a bug within the Python JSON decoder implementation that kept the parsed-string cache from emptying once decoding completed. Based on a patch from c-fos.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
