# token: `token.ERRORTOKEN`, `token.N_TOKENS`, `token.EXACT_TOKEN_TYPES`

token.ERRORTOKEN

Token value used to indicate wrong input.

As a rule the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module flags errors by raising exceptions rather than emitting this token. It can equally emit tokens like `OP` or `NAME` whose strings the parser later turns down.

The remaining tokens stand for particular [operators](https://docs.python.org/3.14/reference/lexical_analysis.html#operators) and [delimiters](https://docs.python.org/3.14/reference/lexical_analysis.html#delimiters). (These get reported by the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module as `OP`; for the particulars, see `exact_type` in the `tokenize` documentation.)

| Token | Value |
| --- | --- |
| token.LPAR | `"("` |
| token.RPAR | `")"` |
| token.LSQB | `"["` |
| token.RSQB | `"]"` |
| token.COLON | `":"` |
| token.COMMA | `","` |
| token.SEMI | `";"` |
| token.PLUS | `"+"` |
| token.MINUS | `"-"` |
| token.STAR | `"*"` |
| token.SLASH | `"/"` |
| token.VBAR | `"|"` |
| token.AMPER | `"&"` |
| token.LESS | `"<"` |
| token.GREATER | `">"` |
| token.EQUAL | `"="` |
| token.DOT | `"."` |
| token.PERCENT | `"%"` |
| token.LBRACE | `"{"` |
| token.RBRACE | `"}"` |
| token.EQEQUAL | `"=="` |
| token.NOTEQUAL | `"!="` |
| token.LESSEQUAL | `"<="` |
| token.GREATEREQUAL | `">="` |
| token.TILDE | `"~"` |
| token.CIRCUMFLEX | `"^"` |
| token.LEFTSHIFT | `"<<"` |
| token.RIGHTSHIFT | `">>"` |
| token.DOUBLESTAR | `"**"` |
| token.PLUSEQUAL | `"+="` |
| token.MINEQUAL | `"-="` |
| token.STAREQUAL | `"*="` |
| token.SLASHEQUAL | `"/="` |
| token.PERCENTEQUAL | `"%="` |
| token.AMPEREQUAL | `"&="` |
| token.VBAREQUAL | `"|="` |
| token.CIRCUMFLEXEQUAL | `"^="` |
| token.LEFTSHIFTEQUAL | `"<<="` |
| token.RIGHTSHIFTEQUAL | `">>="` |
| token.DOUBLESTAREQUAL | `"**="` |
| token.DOUBLESLASH | `"//"` |
| token.DOUBLESLASHEQUAL | `"//="` |
| token.AT | `"@"` |
| token.ATEQUAL | `"@="` |
| token.RARROW | `"->"` |
| token.ELLIPSIS | `"..."` |
| token.COLONEQUAL | `":="` |
| token.EXCLAMATION | `"!"` |

These non-token constants are supplied:

 token.N_TOKENS

The number of token types defined in this module.

 token.EXACT_TOKEN_TYPES

A dictionary that maps each token's string representation onto its numeric code.

Added in version 3.8.

Changed in version 3.5: Introduced the `AWAIT` and `ASYNC` tokens.

Changed in version 3.7: Introduced the `COMMENT`, `NL` and `ENCODING` tokens.

Changed in version 3.7: Dropped the `AWAIT` and `ASYNC` tokens. The words "async" and "await" now tokenize as `NAME` tokens.

Changed in version 3.8: Introduced `TYPE_COMMENT`, `TYPE_IGNORE`, `COLONEQUAL`. Brought the `AWAIT` and `ASYNC` tokens back (they are required so that parsing of older Python versions works for [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) when `feature_version` is set to 6 or below).

Changed in version 3.12: Introduced `EXCLAMATION`.

Changed in version 3.13: Dropped the `AWAIT` and `ASYNC` tokens once more.

[Subject index](INDEX.md) · [Previous](token-fstring-end-to-token-soft-keyword.md) · [Continue](../tokenize/tokenize-tokenizer-for-python-source.md) · [Owning module, declaration or section: token](token-tok-name-to-token-fstring-middle.md)
