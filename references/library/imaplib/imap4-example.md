# imaplib - IMAP4 Example

### IMAP4 Example

What follows is a minimal example (with no error checking) that opens a mailbox, then retrieves and prints every message:

```python
import getpass, imaplib

M = imaplib.IMAP4(host='example.org')
M.login(getpass.getuser(), getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()

```

[Subject index](INDEX.md) · [Previous](imap4-protocol-version-to-imap4-utf8-enabled.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md)
