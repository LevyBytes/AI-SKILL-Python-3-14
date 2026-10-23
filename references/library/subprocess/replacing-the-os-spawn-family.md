# subprocess - Replacing the `os.spawn` family

### Replacing the [`os.spawn`](https://docs.python.org/3.14/library/os.html#os.spawnl) family

P_NOWAIT example:

```python
pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
==>
pid = Popen(["/bin/mycmd", "myarg"]).pid

```

P_WAIT example:

```python
retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
==>
retcode = call(["/bin/mycmd", "myarg"])

```

Vector example:

```python
os.spawnvp(os.P_NOWAIT, path, args)
==>
Popen([path] + args[1:])

```

Environment example:

```python
os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
==>
Popen(["/bin/mycmd", "myarg"], env={"PATH": "/usr/bin"})

```

[Subject index](INDEX.md) · [Previous](replacing-os-system.md) · [Continue](replacing-os-popen.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
