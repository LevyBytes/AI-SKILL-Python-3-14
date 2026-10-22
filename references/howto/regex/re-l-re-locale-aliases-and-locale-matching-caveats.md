# re.L / re.LOCALE aliases and locale matching caveats

re.L

 re.LOCALE
Make `\w`, `\W`, `\b`, `\B` and case-insensitive matching depend on the active locale rather than on the Unicode database.

A locale is a C-library facility that exists to assist authors of programs that need to respect differences between languages. As an illustration, when you handle encoded French text, being able to write `\w+` to capture words is convenient, yet `\w` matches only the character class `[A-Za-z]` for bytes patterns; bytes that stand for `é` or `ç` won't be matched. Given a correctly configured system with a French locale active, particular C functions will report to the program that the byte standing for `é` ought to count as a letter too. Applying the [`LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) flag at compile time for a regular expression makes the compiled object rely on those C functions for `\w`; the tradeoff is reduced speed, though `\w+` then matches French words the way you'd want. Relying on this flag is not recommended under Python 3 since the locale machinery is highly unreliable, deals with just a single "culture" per run, and supports only 8-bit locales. For Unicode (str) patterns, Python 3 turns on Unicode matching by default, and that handling copes with assorted locales/languages.

[Subject index](INDEX.md) · [Previous source owning section](compilation-flags.md) · [Compilation flags](compilation-flags.md) · [Previous source context](compilation-flags.md) · [Compilation flags continuation](compilation-flags-continuation.md) · [Previous source context](compilation-flags-continuation.md) · [Following source context](compilation-flags-continuation.md)
