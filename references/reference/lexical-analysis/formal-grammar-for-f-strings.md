# 2.5.9. Formal grammar for f-strings

### 2.5.9. Formal grammar for f-strings

Responsibility for f-strings is divided: the [lexical analyzer](https://docs.python.org/3.14/glossary.html#term-lexical-analyzer) emits the tokens [`FSTRING_START`](https://docs.python.org/3.14/library/token.html#token.FSTRING_START), [`FSTRING_MIDDLE`](https://docs.python.org/3.14/library/token.html#token.FSTRING_MIDDLE) and [`FSTRING_END`](https://docs.python.org/3.14/library/token.html#token.FSTRING_END), while the parser takes care of the expressions inside the replacement field. Precisely how that split happens is a CPython implementation detail.

Accordingly, the grammar for f-strings blends together [lexical and syntactic definitions](https://docs.python.org/3.14/reference/introduction.html#notation-lexical-vs-syntactic).

These are the cases where whitespace carries meaning:

- Inside [`FSTRING_START`](https://docs.python.org/3.14/library/token.html#token.FSTRING_START) (between the prefix and quote) no whitespace may appear.

- Whitespace found in [`FSTRING_MIDDLE`](https://docs.python.org/3.14/library/token.html#token.FSTRING_MIDDLE) belongs to the contents of the literal string.

- Within `fstring_replacement_field`, when `f_debug_specifier` appears, every bit of whitespace running from the opening brace up to the `f_debug_specifier`, plus the whitespace right after `f_debug_specifier`, is kept as part of the expression.

**CPython implementation detail:** Tokenization does not process the expression; rather, it is pulled out of the source code by using the positions of the `{` token and the token following `=`.

To flag special characters (backslash, newline, `{`, `}`) and sequences (`f_quote`), the `FSTRING_MIDDLE` definition relies on [negative lookaheads](https://docs.python.org/3.14/reference/introduction.html#lexical-lookaheads) (`!`).

```text

fstring:    FSTRING_START fstring_middle* FSTRING_END

FSTRING_START:      fstringprefix ("'" | '"' | "'''" | '"""')
FSTRING_END:        f_quote
fstringprefix:      <("f" | "fr" | "rf"), case-insensitive>
f_debug_specifier:  '='
f_quote:            <the quote character(s) used in FSTRING_START>

fstring_middle:
   | fstring_replacement_field
   | FSTRING_MIDDLE
FSTRING_MIDDLE:
   | (!"\" !newline !'{' !'}' !f_quote) source_character
   | stringescapeseq
   | "{{"
   | "}}"
   | <newline, in triple-quoted f-strings only>
fstring_replacement_field:
   | '{' f_expression [f_debug_specifier] [fstring_conversion]
         [fstring_full_format_spec] '}'
fstring_conversion:
   | "!" ("s" | "r" | "a")
fstring_full_format_spec:
   | ':' fstring_format_spec*
fstring_format_spec:
   | FSTRING_MIDDLE
   | fstring_replacement_field
f_expression:
   | ','.(conditional_expression | "*" or_expr)+ [","]
   | yield_expression
```

Note

Within the grammar snippet above, the `f_quote` and `FSTRING_MIDDLE` rules are context-sensitive – what they match hinges on the contents of the `FSTRING_START` belonging to the closest enclosing `fstring`.

Building a more conventional formal grammar out of this template is left to the reader as an exercise.

T-strings share their grammar with f-strings, swapping *t* for *f* at the start of the rule and token names as well as in the prefix.

```text

tstring:    TSTRING_START tstring_middle* TSTRING_END

<rest of the t-string grammar is omitted; see above>
```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](t-strings.md) · [Following source section](numeric-literals.md)
