# poplib - POP3 Example

### POP3 Example

What follows is a bare-bones example (skipping error handling) that opens a mailbox, then fetches and prints every message:

```python
import getpass, poplib

M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)

```

Down at the bottom of the module sits a test section holding a fuller worked example.

[Subject index](INDEX.md) · [Previous](pop3-stls.md) · [Continue](../posix/posix-the-most-common-posix-system-calls.md) · [Owning module, declaration or section: poplib](poplib-pop3-class.md)
