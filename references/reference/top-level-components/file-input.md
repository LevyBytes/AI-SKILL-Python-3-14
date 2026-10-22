# 9.2. File input

### 9.2. File input

Every bit of input taken from non-interactive files shares one common shape:

```text

file_input: (NEWLINE | statement)* ENDMARKER
```

You will encounter this syntax in the cases listed here:

- while reading a complete Python program, whether it comes from a file or a string;

- while reading a module;

- while reading a string handed to the [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) function;

[Subject index](INDEX.md) · [Owning language section](top-level-components.md) · [Previous source section](complete-python-programs.md) · [Following source section](interactive-input.md)
