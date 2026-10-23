# locale - Background, details, hints, tips and caveats

### Background, details, hints, tips and caveats

The C standard frames the locale as a program-wide property that may be comparatively costly to change. Beyond that, some implementations are broken in a way that makes frequent locale changes liable to cause core dumps. All of this makes the locale somewhat painful to use correctly.

At the outset, once a program is started, the locale is the `C` locale, regardless of whatever the user's preferred locale is. One exception applies: at startup the `LC_CTYPE` category is changed so that the current locale encoding matches the user's preferred locale encoding. By calling `setlocale(LC_ALL, '')`, the program must explicitly state that it wants the user's preferred locale settings for the other categories.

Calling `setlocale()` inside some library routine is generally a poor idea, since as a side effect it touches the whole program. Saving and restoring it is nearly as poor: it is costly and touches other threads that happen to run before the settings have been restored.

When coding a module for general use, if you need a locale independent version of an operation that the locale affects (for example, particular formats fed to [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime)), you will have to find a way of doing it without the standard library routine. Better still is to convince yourself that relying on locale settings is acceptable. Only as a final resort should you document that your module is incompatible with non-`C` locale settings.

The sole way to carry out numeric operations per the locale is to use the special functions this module defines: `atof()`, `atoi()`, `format_string()`, `str()`.

There is no way to perform case conversions and character classifications per the locale. For (Unicode) text strings these proceed by the character value alone, whereas for byte strings, the conversions and classifications proceed by the byte's ASCII value, and bytes whose high bit is set (that is, non-ASCII bytes) are never converted nor counted as part of a character class such as letter or whitespace.

[Subject index](INDEX.md) · [Previous](locale-str-to-locale-char-max.md) · [Continue](locale-names.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
