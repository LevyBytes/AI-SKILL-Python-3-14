# 4.9.3.2. Positional-Only Parameters

#### 4.9.3.2. Positional-Only Parameters

Examining this more closely, certain parameters can be flagged as *positional-only*. For a *positional-only* parameter, sequence is significant and you cannot name it with a keyword. Such parameters sit ahead of a `/` (forward-slash). That `/` serves to draw a logical boundary between the positional-only group and everything after it. Absent any `/` in the definition, the function has no positional-only parameters at all.

Whatever comes after the `/` is allowed to be *positional-or-keyword* or *keyword-only*.

[Subject index](INDEX.md) · [Previous source section](positional-or-keyword-arguments.md) · [Following source section](keyword-only-arguments.md)
