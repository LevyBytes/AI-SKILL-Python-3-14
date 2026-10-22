# subprocess — Replacing **/bin/sh** shell command substitution

### Replacing **/bin/sh** shell command substitution

```bash
output=$(mycmd myarg)

```

becomes:

```python
output = check_output(["mycmd", "myarg"])

```

[Subject index](INDEX.md) · [Previous](replacing-older-functions-with-the-subprocess-module.md) · [Continue](replacing-shell-pipeline.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
