# Python 3.14.1 final / library / functions and types

[gh-138239](https://github.com/python/cpython/issues/138239): Within [type statements](https://docs.python.org/3.14/reference/simple_stmts.html#type), the REPL now treats [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) as a highlighted soft keyword.

[gh-138891](https://github.com/python/cpython/issues/138891): Resolves a `SyntaxError` raised by `inspect.get_annotations(f, eval_str=True)` against a function whose annotation is a [**PEP 646**](https://peps.python.org/pep-0646/) `star_expression`

[gh-140590](https://github.com/python/cpython/issues/140590): Tightens argument validation for `functools.partial.__setstate__()`, which could otherwise corrupt internal state and crash. Sergey Miryanov authored the patch.

[gh-140797](https://github.com/python/cpython/issues/140797): Lexicon patterns supplied to the undocumented `re.Scanner` class may no longer carry capturing groups in their regular expressions. Earlier on, capturing-group patterns risked crashing with a segmentation fault. Reach instead for non-capturing groups (?:?).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
