# subprocess — Replacing `os.popen()`

### Replacing [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen)

Here is how handling of the return code maps over:

```python
pipe = os.popen(cmd, 'w')
...
rc = pipe.close()
if rc is not None and rc >> 8:
    print("There were some errors")
==>
process = Popen(cmd, stdin=PIPE)
...
process.stdin.close()
if process.wait() != 0:
    print("There were some errors")

```

[Subject index](INDEX.md) · [Previous](replacing-the-os-spawn-family.md) · [Continue](subprocess-getstatusoutput-to-subprocess-getoutput.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
