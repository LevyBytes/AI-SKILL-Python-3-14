# Why can’t raw strings (r-strings) end with a backslash?

### Why can’t raw strings (r-strings) end with a backslash?

Stated more carefully, the problem is an odd count of trailing backslashes: that final, unpaired backslash escapes the closing quote, so the string is never terminated.

The whole point of raw strings is to make it simpler to feed input to processors — regular expression engines above all — that prefer to handle backslash escapes themselves. Since those processors already treat a dangling, unmatched backslash as an error, raw strings forbid it. In exchange, they let you smuggle the string’s quote character through by escaping it with a backslash. The rules hold up nicely whenever r-strings are put to the use they were meant for.

Constructing Windows pathnames? Bear in mind that every Windows system call takes forward slashes just as readily:

```python
f = open("/mydir/file.txt")  # works fine!

```

And when you need a pathname destined for a DOS command, one of these approaches works:

```python
dir = r"\this\is\my\dos\dir" "\\"
dir = r"\this\is\my\dos\dir\ "[:-1]
dir = "\\this\\is\\my\\dos\\dir\\"

```

[Subject index](INDEX.md)
