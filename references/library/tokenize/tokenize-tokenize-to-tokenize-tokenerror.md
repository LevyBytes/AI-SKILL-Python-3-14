# tokenize - Tokenizing Input

### Tokenizing Input

A [generator](https://docs.python.org/3.14/glossary.html#term-generator) serves as the primary entry point:

 tokenize.tokenize(*readline*)

The `tokenize()` generator takes a single argument, *readline*, which has to be a callable object presenting the same interface as the [`io.IOBase.readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) method of file objects. Every call to the function ought to give back one line of input as bytes.

The generator yields 5-tuples whose members are: the token type; then the token string; then a 2-tuple `(srow, scol)` of ints pinning down the row and column at which the token begins in the source; then a 2-tuple `(erow, ecol)` of ints pinning down the source row and column at the token's end; and last the line where the token showed up. That line handed along (the closing tuple item) is the *physical* line. The 5 tuple comes back as a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying the field names: `type string start end line`.

The [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) returned carries an extra property called `exact_type` that holds the exact operator type for [`OP`](https://docs.python.org/3.14/library/token.html#token.OP) tokens. For every other token type, `exact_type` matches the named tuple `type` field.

Changed in version 3.1: Added support for named tuples.

Changed in version 3.3: Added support for `exact_type`.

`tokenize()` works out the file's source encoding by hunting for a UTF-8 BOM or encoding cookie, in keeping with [**PEP 263**](https://peps.python.org/pep-0263/).

 tokenize.generate_tokens(*readline*)

Tokenize a source reading unicode strings instead of bytes.

As with `tokenize()`, the *readline* argument is a callable that gives back a single line of input. The difference is that `generate_tokens()` expects *readline* to give back a str object rather than bytes.

What you get is an iterator that yields named tuples, precisely as `tokenize()` does. It does not yield an [`ENCODING`](https://docs.python.org/3.14/library/token.html#token.ENCODING) token.

Every constant from the [`token`](https://docs.python.org/3.14/library/token.html#module-token) module is exported from `tokenize` as well.

One more function is offered to undo the tokenization process. It comes in handy for building tools that tokenize a script, alter the token stream, and write the altered script back out.

 tokenize.untokenize(*iterable*)

Turn tokens back into Python source code. The *iterable* has to give back sequences holding at least two elements, the token type and the token string. Any further sequence elements get ignored.

The outcome is guaranteed to tokenize back so as to match the input, which makes the conversion lossless and round-trips dependable. That guarantee covers only the token type and token string, since the spacing between tokens (column positions) may shift.

It gives back bytes, encoded with the [`ENCODING`](https://docs.python.org/3.14/library/token.html#token.ENCODING) token, which is the first token sequence that `tokenize()` outputs. Where the input has no encoding token, it gives back a str instead.

`tokenize()` has to figure out the encoding of the source files it tokenizes. The function it leans on to do this is available:

 tokenize.detect_encoding(*readline*)

The `detect_encoding()` function serves to detect which encoding ought to be used to decode a Python source file. It takes one argument, readline, in the same fashion as the `tokenize()` generator.

It will invoke readline no more than two times, then give back the encoding it found (as a string) together with a list holding whatever lines (left undecoded from bytes) it took in.

It picks up the encoding from a UTF-8 BOM or an encoding cookie as spelled out in [**PEP 263**](https://peps.python.org/pep-0263/). Where both a BOM and a cookie appear but clash, a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) gets raised. Bear in mind that when the BOM is found, `'utf-8-sig'` comes back as an encoding.

Where no encoding is specified, the default of `'utf-8'` comes back.

Use `open()` to open Python source files: it leans on `detect_encoding()` to detect the file encoding.

 tokenize.open(*filename*)

Open a file in read only mode using the encoding detected by `detect_encoding()`.

Added in version 3.2.

 *exception *tokenize.TokenError

Gets raised when either a docstring or an expression that may break across several lines never reaches completion anywhere in the file, for instance:

```python
"""Beginning of
docstring

```

or:

```python
[1,
 2,
 3

```

[Subject index](INDEX.md) · [Previous](tokenize-tokenizer-for-python-source.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: tokenize](tokenize-tokenizer-for-python-source.md)
