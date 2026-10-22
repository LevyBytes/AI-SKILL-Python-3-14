# smtplib — SMTP Example

### SMTP Example

This example asks the user for the addresses required in the message envelope (the ‘To’ and ‘From’ addresses), plus the message to be delivered. Note that whatever headers belong with the message have to be included in the message as it is entered; this example performs no processing of the [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) headers. In particular, the ‘To’ and ‘From’ addresses must appear explicitly in the message headers:

```python
import smtplib

def prompt(title):
    return input(title).strip()

from_addr = prompt("From: ")
to_addrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
lines = [f"From: {from_addr}", f"To: {', '.join(to_addrs)}", ""]
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        lines.append(line)

msg = "\r\n".join(lines)
print("Message length is", len(msg))

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_addr, to_addrs, msg)
server.quit()

```

Note

As a rule, you will want to lean on the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package’s features to assemble an email message, which you can then dispatch via `send_message()`; see [email: Examples](https://docs.python.org/3.14/library/email.examples.html#email-examples).

[Subject index](INDEX.md) · [Previous](smtp-sendmail-to-smtp-esmtp-features.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md)
