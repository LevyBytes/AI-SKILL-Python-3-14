# locale - Locale names

### Locale names

The format of the locale name depends on the platform, and the set of supported locales can hinge on the system configuration.

On Posix platforms, it usually takes the format [1]:

```

  language ["_" territory] ["." charset] ["@" modifier]

```

here *language* gives a two- or three-letter language code drawn from [ISO 639](https://www.iso.org/iso-639-language-code); *territory* gives a two-letter country or region code drawn from [ISO 3166](https://www.iso.org/iso-3166-country-codes.html); *charset* names a locale encoding; and *modifier* names a script, a language subtag, a sort order identifier, or another locale modifier (for example, "latin", "valencia", "stroke" and "euro").

On Windows, several formats are supported. [2] [3] A subset of [IETF BCP 47](https://www.rfc-editor.org/info/bcp47) tags:

```

  language ["-" script] ["-" territory] ["." charset]
  language ["-" script] "-" territory "-" modifier

```

here *language* and *territory* carry the meaning they hold in Posix; *script* gives a four-letter script code drawn from [ISO 15924](https://www.unicode.org/iso15924/); and *modifier* names a language subtag, a sort order identifier or a custom modifier (for example, "valencia", "stroke" or "x-python"). Both the hyphen (`'-'`) and underscore (`'_'`) separators are supported. UTF-8 is the only encoding allowed for BCP 47 tags.

Windows also supports locale names in the format:

```

  language ["_" territory] ["." charset]

```

here *language* and *territory* spell out full names, like "English" and "United States", while *charset* holds either a code page number (for example, "1252") or UTF-8. Within this format the underscore separator alone is supported.

The "C" locale is supported on all platforms.

[Subject index](INDEX.md) · [Previous](background-details-hints-tips-and-caveats.md) · [Continue](for-extension-writers-and-programs-that-embed-python.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
