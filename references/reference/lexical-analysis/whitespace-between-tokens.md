# 2.1.9. Whitespace between tokens

### 2.1.9. Whitespace between tokens

Apart from the start of a logical line and inside string literals, the whitespace characters space, tab and formfeed are interchangeable as token separators:

```text

whitespace:  ' ' | tab | formfeed
```

Two tokens require whitespace between them only when joining them could otherwise read as some other token. For instance, `ab` is a single token, whereas `a b` is a pair of tokens. Yet both `+a` and `+ a` yield two tokens, `+` and `a`, because `+a` is not a legal token.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](indentation.md) · [Following source section](end-marker.md)
