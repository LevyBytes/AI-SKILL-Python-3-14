# Locale integration with gettext catalogs

In most cases a Python program has no reason to call these routines at all; reaching for [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) is the recommended path. One well-understood exception involves programs that are linked against extra C libraries which, behind the scenes, call the C-level `gettext` or `dcgettext` functions. With such programs, binding the text domain can become necessary so those libraries are able to find the right message catalogs.

[Subject index](INDEX.md)
