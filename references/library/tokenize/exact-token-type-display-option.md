# tokenize - Examples - Contract: The exact token type names can be displayed using the `-e` option:

The exact token type names can be displayed using the `-e` option:

```shell
$ python -m tokenize -e hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:          LPAR           '('
1,14-1,15:          RPAR           ')'
1,15-1,16:          COLON          ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           LPAR           '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          RPAR           ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           LPAR           '('
4,10-4,11:          RPAR           ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''

```

Example of tokenizing a file from code, taking in unicode strings rather than bytes by way of `generate_tokens()`:

```python
import tokenize

with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)

```

Or reading bytes directly with `tokenize()`:

```python
import tokenize

with open('hello.py', 'rb') as f:
    tokens = tokenize.tokenize(f.readline)
    for token in tokens:
        print(token)

```

[Subject index](INDEX.md) · [Previous](examples-section-introduction-and-initial-examples.md) · [Continue](../tomllib/tomllib-load-to-tomllib-tomldecodeerror.md) · [Owning module, declaration or section: tokenize](tokenize-tokenizer-for-python-source.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md)
