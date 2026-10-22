# subprocess — Replacing shell pipeline

### Replacing shell pipeline

```bash
output=$(dmesg | grep hda)

```

becomes:

```python
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]

```

Invoking `p1.stdout.close()` once p2 is up and running matters, because it lets p1 get a SIGPIPE should p2 finish ahead of p1.

As another option, when the input is trusted, you can still lean on the shell’s built-in pipeline support outright:

```bash
output=$(dmesg | grep hda)

```

becomes:

```python
output = check_output("dmesg | grep hda", shell=True)

```

[Subject index](INDEX.md) · [Previous](replacing-bin-sh-shell-command-substitution.md) · [Continue](replacing-os-system.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
