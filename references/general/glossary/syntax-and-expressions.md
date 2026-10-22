# Syntax and expressions

Open when checking Python definitions for syntax and expressions.

## token

A small piece of source code, turned out by the [lexical analyzer](https://docs.python.org/3.14/reference/lexical_analysis.html#lexical) (which also goes by *tokenizer*). Names, numbers, strings, operators, newlines and the like are stood for by tokens.

The [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module surfaces Python's lexical analyzer. The [`token`](https://docs.python.org/3.14/library/token.html#module-token) module holds information about the assorted kinds of tokens.

## lexical analyzer

The formal designation for the *tokenizer*; see token.

## statement

A statement makes up one piece of a suite (that is, a "block" of code). Any statement is either an expression or else one of several keyword-based constructs, among them [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) or [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for).

## expression

A fragment of syntax reducible to a value. Said differently, an expression gathers expression components ? literals, names, attribute access, operators, or function calls ? each of which yields a value. Unlike numerous other languages, Python does not treat every language construct as an expression. Certain statements may not stand in as expressions, [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) being one. Assignments, too, count as statements and not expressions.

## floor division

Arithmetic division that truncates downward to the closest integer. `//` is the floor division operator. As an example, `11 // 4` works out to `2`, whereas float true division would hand back `2.75`. Observe that `(-11) // 4` comes to `-3`, since `-2.75` rounds *downward* to that. See [**PEP 238**](https://peps.python.org/pep-0238/).

## walrus operator

A playful nickname for the [assignment expression](https://docs.python.org/3.14/reference/expressions.html#assignment-expressions) operator `:=`, owing to its faint resemblance to a walrus once you tilt your head.

## f-string

f-strings

String literals carrying an `f` or `F` prefix are widely termed "f-strings", a shorthand for [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings). See also [**PEP 498**](https://peps.python.org/pep-0498/).

## t-string

t-strings

String literals carrying a `t` or `T` prefix are widely known as "t-strings", which abbreviates [template string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings).

## triple-quoted string

A string fenced by three copies of either a quotation mark (") or an apostrophe ('). Although they offer no capability that single-quoted strings lack, they come in handy for several reasons. They let you drop in unescaped single and double quotes inside a string, and they can run across several lines without need of the continuation character, which makes them especially handy when you are writing docstrings.

## docstring

A string literal occurring as the very first expression within a module, function, or class. Although it is skipped during execution of the suite, the compiler picks it up and stores it in the [`__doc__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__doc__) attribute of the surrounding module, function, or class. Because introspection exposes it, this is the standard location for an object's documentation.

## __future__

A [future statement](https://docs.python.org/3.14/reference/simple_stmts.html#future), `from __future__ import <feature>`, instructs the compiler to compile the present module with syntax or semantics slated to become standard in some later Python release. Possible *feature* values are documented by the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) module. Import that module and inspect its variables, and you can find out which release first introduced a given feature and which release made (or will make) it the default:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

```

[Glossary context index](INDEX.md).
