# 6.2.4. Parenthesized forms

### 6.2.4. Parenthesized forms

A parenthesized form wraps an optional expression list inside parentheses:

```text

parenth_form: "(" [starred_expression] ")"
```

Whatever its enclosed expression list produces is what a parenthesized expression list produces: when the list holds one or more commas it produces a tuple; otherwise it produces just the single expression composing that expression list.

A pair of parentheses with nothing inside produces an empty tuple object. As tuples are immutable, the literal rules carry over (so two appearances of the empty tuple might or might not produce the same object).

Bear in mind that it is the comma ? not the parentheses ? that builds a tuple. The lone exception is the empty tuple, which *does* require parentheses, since permitting an unparenthesized ?nothing? inside expressions would introduce ambiguities and let frequent typos slip by undetected.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](string-literal-concatenation.md) · [Following source section](displays-for-lists-sets-and-dictionaries.md)
