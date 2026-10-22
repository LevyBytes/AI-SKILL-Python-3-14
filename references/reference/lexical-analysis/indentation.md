# 2.1.8. Indentation

### 2.1.8. Indentation

The leading whitespace (spaces and tabs) at a logical line's start serves to figure out that line's indentation level, and that level in turn governs how statements are grouped.

Each tab gets expanded (left to right) into one through eight spaces so that the count of characters up to and including the substitution reaches a multiple of eight (the intent is to match the rule Unix applies). The line's indentation is then set by the count of spaces ahead of the first non-blank character. Backslashes cannot be used to spread indentation over multiple physical lines; the whitespace preceding the first backslash fixes the indentation.

When a source file blends tabs and spaces so that meaning would hinge on the value of a tab measured in spaces, the indentation is treated as inconsistent and rejected; under those conditions a [`TabError`](https://docs.python.org/3.14/library/exceptions.html#TabError) is raised.

**Cross-platform compatibility note:** given how text editors behave on non-UNIX platforms, mixing spaces and tabs for indentation within one source file is unwise. Be aware too that some platforms may put an explicit cap on the maximum indentation level.

The line may open with a formfeed character; the indentation calculations described above disregard it. Where formfeed characters show up elsewhere within the leading whitespace, their effect is undefined (they might, for example, drop the space count back to zero).

A stack is used to turn the indentation levels of successive lines into [`INDENT`](https://docs.python.org/3.14/library/token.html#token.INDENT) and [`DEDENT`](https://docs.python.org/3.14/library/token.html#token.DEDENT) tokens, in the following manner.

Ahead of reading the file's first line, a lone zero is placed on the stack; it never gets popped back off. From bottom to top the numbers on the stack are always strictly increasing. As each logical line starts, that line's indentation level gets matched against the stack's top. Equality means nothing happens. A larger value gets pushed on the stack and yields one `INDENT` token. A smaller value *must* match one of the numbers already on the stack; every larger number on the stack is popped off, and each pop produces a `DEDENT` token. When the file ends, one `DEDENT` token is produced for each number still on the stack that exceeds zero.

What follows is a sample of correctly (if bewilderingly) indented Python code:

```python
def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r

```

This next sample illustrates a range of indentation errors:

```python
 def perm(l):                       # error: first line indented
for i in range(len(l)):             # error: not indented
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # error: unexpected indent
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # error: inconsistent dedent

```

(In fact the parser catches the first three errors; only the final one is caught by the lexical analyzer — the indentation of `return r` fails to line up with any level popped from the stack.)

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](blank-lines.md) · [Following source section](whitespace-between-tokens.md)
