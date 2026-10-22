# 1.2. Notation

### 1.2. Notation

Wherever the lexical layer and the grammar get described, the notation in play blends [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) together with [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar). Consider this:

```text

name:   letter (letter | digit | "_")*
letter: "a"..."z" | "A"..."Z"
digit:  "0"..."9"
```

Reading the opening line of that snippet, a `name` consists of one `letter` trailed by a run holding none or any quantity of `letter`s, `digit`s, plus underscores. Each `letter`, for its part, stands for one of the lone characters spanning `'a'` up to `'z'` along with `A` up to `Z`; a `digit` denotes a solitary character drawn from `0` through `9`.

Every rule opens with a name (the label that tells you which rule is under definition) and then a colon, `:`. Whatever sits on the colon's right side, forming the definition, draws on these syntax elements:

- `name`: Here a name points at some other rule. Whenever it can, it doubles as a link leading to where that rule is defined.

  - `TOKEN`: A name in capitals designates a [token](https://docs.python.org/3.14/glossary.html#term-token). As far as grammar definitions go, a token counts as nothing other than a rule.

- `"text"`, `'text'`: Whatever sits inside single or double quotes has to be matched word-for-word (leaving the quotes themselves out). Which quote style gets used hinges on what the `text` signifies:

  - `'if'`: When a name appears within single quotes, it marks a [keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#keywords).

  - `"case"`: When a name appears within double quotes, it marks a [soft-keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

  - `'@'`: Should a non-letter symbol sit inside single quotes, it stands for an [`OP`](https://docs.python.org/3.14/library/token.html#token.OP) token — in other words, either a [delimiter](https://docs.python.org/3.14/reference/lexical_analysis.html#delimiters) or an [operator](https://docs.python.org/3.14/reference/lexical_analysis.html#operators).

- `e1 e2`: When items have nothing but whitespace dividing them, that spells out a sequence. In this case, `e2` has to come right after `e1`.

- `e1 | e2`: Alternatives get split apart by a vertical bar. What it captures is PEG's notion of “ordered choice”: once `e1` matches, `e2` never gets examined. Conventional PEG grammars spell this with a slash, `/`, in place of the vertical bar. Turn to [**PEP 617**](https://peps.python.org/pep-0617/) for fuller context and the finer points.

- `e*`: A star stands for the item ahead of it repeating any number of times, including none.

- `e+`: In the same vein, a plus stands for the item repeating at least once.

- `[e]`: Wrapping a phrase in square brackets signals that it shows up either not at all or just once. Put another way, the bracketed phrase may be left out.

- `e?`: A trailing question mark carries the very meaning that square brackets do: whatever item sits in front of it can be omitted.

- `(e)`: Grouping is what parentheses serve to do.

What follows is notation that comes into play solely within lexical definitions.

- `"a"..."z"`: A pair of literal characters with three dots between them stands for picking any one character falling inside that stated (endpoints included) span of ASCII characters.

- `<...>`: Placing a phrase within angle brackets supplies a loose, plain-language account of whatever symbol is being matched (say, `<any ASCII character except "\">`), or else a shorthand spelled out somewhere in the surrounding text (say, `<Lu>`).

A number of definitions reach for *lookaheads* as well; these mark that some element is required to match (or required not to) at a particular spot, all while leaving the input untouched:

- `&e`: this is a positive lookahead — meaning `e` has to match

- `!e`: this is a negative lookahead — meaning `e` is required *not* to match

Among the unary operators (`*`, `+`, `?`), binding is as tight as it can get, whereas the vertical bar (`|`) is the loosest-binding of all.

The single role whitespace plays is keeping tokens apart from one another.

Typically a rule fits within one line, though any rule running too long is allowed to wrap across several:

```text

literal: stringliteral | bytesliteral
         | integer | floatnumber | imagnumber
```

As another option, you can lay out a rule so its opening line stops at the colon, with every alternative then starting on its own fresh line behind a vertical bar. Take this:

```text

literal:
   | stringliteral
   | bytesliteral
   | integer
   | floatnumber
   | imagnumber
```

By no means should this be read as implying a blank opening alternative.

[Subject index](INDEX.md) · [Owning language section](introduction.md) · [Previous source section](alternate-implementations.md) · [Following source section](lexical-and-syntactic-definitions.md)
