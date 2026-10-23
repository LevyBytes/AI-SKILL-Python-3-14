# re - Writing a Tokenizer

### Writing a Tokenizer

A [tokenizer or scanner](https://en.wikipedia.org/wiki/Lexical_analysis) examines a string in order to sort runs of characters into categories — a handy opening move when you set out to build a compiler or interpreter.

Regular expressions define each text category. The approach is to merge them all into one master regular expression, then iterate across the matches one after another:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/re.html#writing-a-tokenizer).

Running the tokenizer yields this output:

```python
Token(type='IF', value='IF', line=2, column=4)
Token(type='ID', value='quantity', line=2, column=7)
Token(type='THEN', value='THEN', line=2, column=16)
Token(type='ID', value='total', line=3, column=8)
Token(type='ASSIGN', value=':=', line=3, column=14)
Token(type='ID', value='total', line=3, column=17)
Token(type='OP', value='+', line=3, column=23)
Token(type='ID', value='price', line=3, column=25)
Token(type='OP', value='*', line=3, column=31)
Token(type='ID', value='quantity', line=3, column=33)
Token(type='END', value=';', line=3, column=41)
Token(type='ID', value='tax', line=4, column=8)
Token(type='ASSIGN', value=':=', line=4, column=12)
Token(type='ID', value='price', line=4, column=15)
Token(type='OP', value='*', line=4, column=21)
Token(type='NUMBER', value=0.05, line=4, column=23)
Token(type='END', value=';', line=4, column=27)
Token(type='ENDIF', value='ENDIF', line=5, column=4)
Token(type='END', value=';', line=5, column=9)

```

    [Frie09]

Friedl, Jeffrey. Mastering Regular Expressions. 3rd ed., O’Reilly Media, 2009. While Python has dropped out of this book's third edition entirely, its first edition went into considerable depth on crafting solid regular expression patterns.

[Subject index](INDEX.md) · [Previous](raw-string-notation.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
