# 2.5.3. Formal grammar

### 2.5.3. Formal grammar

Every string literal apart from “f-strings” and “t-strings” is described by the lexical definitions below.

To signal that a closing quote ends the literal, these definitions employ [negative lookaheads](https://docs.python.org/3.14/reference/introduction.html#lexical-lookaheads) (`!`).

```text

STRING:          [stringprefix] (stringcontent)
stringprefix:    <("r" | "u" | "b" | "br" | "rb"), case-insensitive>
stringcontent:
   | "'''" ( !"'''" longstringitem)* "'''"
   | '"""' ( !'"""' longstringitem)* '"""'
   | "'" ( !"'" stringitem)* "'"
   | '"' ( !'"' stringitem)* '"'
stringitem:      stringchar | stringescapeseq
stringchar:      <any source_character, except backslash and newline>
longstringitem:  stringitem | newline
stringescapeseq: "\" <any source_character>
```

Bear in mind that, as holds for all lexical definitions, whitespace matters. Specifically, the starting quote has to come directly after the prefix (when one is present).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](string-prefixes.md) · [Following source section](escape-sequences.md)
