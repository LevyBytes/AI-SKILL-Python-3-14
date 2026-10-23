# shlex - Parsing Rules

### Parsing Rules

While running outside POSIX mode, `shlex` attempts to follow these rules.

- Quote characters go unrecognized inside words (so `Do"Not"Separate` parses as the lone word `Do"Not"Separate`);

- Escape characters go unrecognized;

- Wrapping characters in quotes keeps the literal value of every character between the quotes;

- A closing quote splits words apart (`"Do"Separate` parses as `"Do"` plus `Separate`);

- With `whitespace_split` at `False`, any character not declared a word character, whitespace, or a quote comes back as a one-character token. Set it to `True` and `shlex` divides words only at whitespace;

- An empty string (`''`) signals EOF;

- Empty strings cannot be parsed, quoted or otherwise.

While running in POSIX mode, `shlex` attempts to follow these parsing rules.

- Quotes get removed and do not split words (`"Do"Not"Separate"` parses as the single word `DoNotSeparate`);

- An unquoted escape character (`'\'`, for instance) keeps the literal value of whichever character comes next;

- Wrapping characters in quotes that fall outside `escapedquotes` (`"'"`, say) keeps the literal value of every character between the quotes;

- Wrapping characters in quotes that belong to `escapedquotes` (`'"'`, say) keeps the literal value of every character between the quotes, save for the characters named in `escape`. Those escape characters keep their special meaning only when followed by the quote currently in use or by the escape character itself; otherwise the escape character is taken as ordinary.

- A [`None`](https://docs.python.org/3.14/library/constants.html#None) value signals EOF;

- Quoted empty strings (`''`) are permitted.

[Subject index](INDEX.md) · [Previous](shlex-source-to-shlex-punctuation-chars.md) · [Continue](improved-compatibility-with-shells.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md)
