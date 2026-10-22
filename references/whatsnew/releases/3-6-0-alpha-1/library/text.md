# Python 3.6.0 alpha 1 / library / text

[bpo-7990](https://bugs.python.org/issue?@action=redirect&bpo=7990): Calling dir() against an ElementTree.Element will now surface its properties — "tag", "text", "tail" and "attrib". Santoso Wijaya wrote the original patch.

[bpo-25873](https://bugs.python.org/issue?@action=redirect&bpo=25873): Iterating ElementTree was optimized. Iterating elements through Element.iter() is now 40% faster, while iterating text through Element.itertext() runs up to 2.5 times faster.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
