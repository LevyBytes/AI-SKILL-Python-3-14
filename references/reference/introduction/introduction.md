# 1. Introduction

## 1. Introduction

### 1. Introduction

What this manual documents is the Python programming language itself; it was never meant to serve as a tutorial.

Although I aim for the greatest accuracy I can manage, I opted for plain English instead of rigorous formal notation everywhere apart from grammar and the lexical layer. That choice keeps the text accessible to a typical reader, though it does open the door to a few unclear spots. As a result, were a visitor from Mars to attempt rebuilding Python using nothing but this text, they would be forced to fill in gaps by guesswork and would most likely arrive at a rather distinct language. That said, whenever you already work in Python and need the exact behavior governing some corner of the language, this is the place where you ought to track it down. Should a stricter formal account appeal to you, perhaps you could donate some hours toward writing one — or build yourself a cloning machine :-).

Loading a language reference with too much information about a specific build carries risk — that build can evolve over time, and rival builds of the very same language might behave in their own ways. Even so, CPython remains the single Python build that sees broad everyday use (even as competing builds keep maturing), and now and then its own peculiarities deserve a mention, above all in spots where the build adds extra restrictions of its own. For that reason, brief “implementation notes” turn up here and there across the pages.

Each Python build ships with a set of built-in plus standard modules. Their documentation lives in [The Python Standard Library](https://docs.python.org/3.14/library/index.html#library-index). A handful of the built-in modules get noted here wherever they touch the definition of the language in a meaningful manner.

[Subject index](INDEX.md) · [Previous source section](../the-python-language-reference/the-python-language-reference-8.md) · [Following source section](alternate-implementations.md)
