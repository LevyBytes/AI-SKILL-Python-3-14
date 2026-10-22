# locale — For extension writers and programs that embed Python

### For extension writers and programs that embed Python

Extension modules should never call `setlocale()`, save to find out what the current locale is. Yet because the return value can be used portably only to restore it, that is not terribly useful (except perhaps to learn whether or not the locale is `C`).

When Python code uses the `locale` module to change the locale, the embedding application feels this too. Should the embedding application not want this to happen, it should strip the `_locale` extension module (the one that does all the work) out of the table of built-in modules in the `config.c` file, and make certain the `_locale` module is not reachable as a shared library.

[Subject index](INDEX.md) · [Previous](locale-names.md) · [Continue](locale-gettext-to-locale-bind-textdomain-codeset.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
