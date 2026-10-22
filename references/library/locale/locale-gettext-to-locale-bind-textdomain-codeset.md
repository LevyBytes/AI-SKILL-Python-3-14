# locale — Access to message catalogs

### Access to message catalogs

 locale.gettext(*msg*)

 locale.dgettext(*domain*, *msg*)

 locale.dcgettext(*domain*, *msg*, *category*)

 locale.textdomain(*domain*)

 locale.bindtextdomain(*domain*, *dir*)

 locale.bind_textdomain_codeset(*domain*, *codeset*)

On systems that offer this interface, the locale module exposes the C library's gettext interface. It is made up of the functions [`gettext()`](https://docs.python.org/3.14/library/gettext.html#module-gettext), `dgettext()`, `dcgettext()`, `textdomain()`, `bindtextdomain()`, and `bind_textdomain_codeset()`. These resemble the same functions in the [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) module, but rely on the C library's binary format for message catalogs, plus the C library's search algorithms for locating message catalogs.

[Subject index](INDEX.md) · [Previous](for-extension-writers-and-programs-that-embed-python.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
