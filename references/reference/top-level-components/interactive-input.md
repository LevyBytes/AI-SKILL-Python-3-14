# 9.3. Interactive input

### 9.3. Interactive input

When in interactive mode, input gets parsed against the grammar shown below:

```text

interactive_input: [stmt_list] NEWLINE | compound_stmt NEWLINE | ENDMARKER
```

Keep in mind that in interactive mode a top-level compound statement has to be trailed by a blank line, which is what lets the parser recognize where the input stops.

[Subject index](INDEX.md) · [Owning language section](top-level-components.md) · [Previous source section](file-input.md) · [Following source section](expression-input.md)
