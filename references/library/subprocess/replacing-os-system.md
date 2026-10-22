# subprocess — Replacing `os.system()`

### Replacing [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system)

```python
sts = os.system("mycmd" + " myarg")
# becomes
retcode = call("mycmd" + " myarg", shell=True)

```

Notes:

- Routing the program through the shell is, as a rule, unnecessary.

- What `call()` returns is encoded in a different fashion from what [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) returns.

- While a command runs, [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) disregards the SIGINT and SIGQUIT signals; with the `subprocess` module, though, the caller has to arrange that on its own.

Something closer to real-world use would read like this:

```python
try:
    retcode = call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)

```

[Subject index](INDEX.md) · [Previous](replacing-shell-pipeline.md) · [Continue](replacing-the-os-spawn-family.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
