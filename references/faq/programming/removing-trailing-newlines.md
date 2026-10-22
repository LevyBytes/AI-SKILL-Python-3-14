# Is there an equivalent to Perl’s `chomp()` for removing trailing newlines from strings?

### Is there an equivalent to Perl’s `chomp()` for removing trailing newlines from strings?

Calling `S.rstrip("\r\n")` strips every occurrence of any line terminator off the end of the string `S` while leaving other trailing whitespace untouched. Should the string `S` span more than one line, with a few empty lines trailing it, the line terminators for all those blank lines are stripped away:

```python
>>> lines = ("line 1 \r\n"
...          "\r\n"
...          "\r\n")
>>> lines.rstrip("\n\r")
'line 1 '

```

Because this is generally only wanted when reading text one line at a time, using `S.rstrip()` in this fashion does the job nicely.

[Subject index](INDEX.md)
