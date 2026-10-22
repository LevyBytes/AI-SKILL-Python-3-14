# 9.4. Expression input

### 9.4. Expression input

Expression input is handled by [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), which discards any leading whitespace. The string you pass to `eval()` is required to take this form:

```text

eval_input: expression_list NEWLINE* ENDMARKER
```

[Subject index](INDEX.md) · [Owning language section](top-level-components.md) · [Previous source section](interactive-input.md)
