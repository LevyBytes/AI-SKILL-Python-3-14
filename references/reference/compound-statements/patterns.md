# 8.6.4. Patterns

### 8.6.4. Patterns

Note

Grammar notation in this section goes beyond plain EBNF:

- the notation `SEP.RULE+` is shorthand for `RULE (SEP RULE)*`

- the notation `!RULE` is shorthand for a negative lookahead assertion

Here is the top-level grammar for `patterns`:

```text

patterns:       open_sequence_pattern | pattern
pattern:        as_pattern | or_pattern
closed_pattern: | literal_pattern
                | capture_pattern
                | wildcard_pattern
                | value_pattern
                | group_pattern
                | sequence_pattern
                | mapping_pattern
                | class_pattern
```

For the sake of illustration, the write-ups that follow each give an ?in simple terms? account of a pattern's behavior (with thanks to Raymond Hettinger, whose document inspired most of these). Keep in mind that such accounts serve only to illustrate and **may not** mirror how things actually work under the hood. On top of that, they leave out some valid forms.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Previous source section](irrefutable-case-blocks.md) · [Following source section](or-patterns.md)
