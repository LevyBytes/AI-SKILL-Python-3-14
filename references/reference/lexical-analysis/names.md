# 2.3. Names (identifiers and keywords)

### 2.3. Names (identifiers and keywords)

*Identifiers*, *keywords*, and *soft keywords* are all represented by [`NAME`](https://docs.python.org/3.14/library/token.html#token.NAME) tokens.

The characters making up names are:

- uppercase and lowercase letters (`A-Z` and `a-z`),

- the underscore (`_`),

- digits (`0` through `9`), which cannot appear as the first character, and

- non-ASCII characters. A valid name is restricted to “letter-like” plus “digit-like” characters alone; consult Non-ASCII characters in names for the specifics.

A name has to hold a minimum of one character, yet faces no maximum length. Case carries meaning.

In formal terms, the lexical definitions below describe names:

```text

NAME:          name_start name_continue*
name_start:    "a"..."z" | "A"..."Z" | "_" | <non-ASCII character>
name_continue: name_start | "0"..."9"
identifier:    <NAME, except keywords>
```

Be aware that this grammar matches some names that are not valid; see Non-ASCII characters in names for details.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Previous source section](other-tokens.md) · [Following source section](keywords.md)
