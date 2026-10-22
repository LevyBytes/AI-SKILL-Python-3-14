# 8. Compound statements

### 8. Compound statements

A compound statement holds (clusters of) further statements inside it, and it governs or directs how those inner statements run. Typically such a statement stretches across several lines, though in its plainest forms an entire compound statement can sit on a single line.

Familiar control-flow mechanisms are provided by the `if`, `while` and `for` statements. The `try` statement designates exception handlers and/or cleanup code that wraps a block of statements, whereas the `with` statement lets setup and teardown code run around an enclosed block. From a syntactic standpoint, definitions of functions and classes count as compound statements too.

Every compound statement is built from one or more ‘clauses.’ A single clause pairs a header with a ‘suite.’ For any given compound statement, all of its clause headers sit at one shared indentation level. Every clause header opens with a keyword that uniquely names it and closes with a colon. The suite is the collection of statements that a clause governs. You can write a suite as one or more semicolon-separated simple statements placed on the same line as the header, right after the header’s colon, or instead as one or more indented statements on the lines that follow. Nested compound statements may appear only in the second of these forms; the snippet below is invalid, chiefly because it would be unclear which `if` clause a trailing `else` clause should attach to:

```python
if test1: if test2: print(x)

```

Be aware, too, that here the semicolon attaches more tightly than the colon, so in the example that follows the [`print()`](https://docs.python.org/3.14/library/functions.html#print) calls all run together or not at all:

```python
if x < y < z: print(x); print(y); print(z)

```

In summary:

```text

compound_stmt: if_stmt
               | while_stmt
               | for_stmt
               | try_stmt
               | with_stmt
               | match_stmt
               | funcdef
               | classdef
               | async_with_stmt
               | async_for_stmt
               | async_funcdef
suite:         stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
statement:     stmt_list NEWLINE | compound_stmt
stmt_list:     simple_stmt (";" simple_stmt)* [";"]
```

Observe that every statement closes with a `NEWLINE`, which a `DEDENT` may then follow. Observe as well that any optional continuation clause opens with a keyword incapable of starting a statement, so no ambiguities arise (Python resolves the ‘dangling `else`’ problem by demanding that nested `if` statements be indented).

For the sake of clarity, the grammar rules shown in the sections below put each clause on its own line.

[Subject index](INDEX.md) · [Following source section](the-if-statement.md)
