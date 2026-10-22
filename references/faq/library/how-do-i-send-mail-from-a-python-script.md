# How do I send mail from a Python script?

### How do I send mail from a Python script?

Reach for the standard library module [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib).

A very basic interactive mail sender built on it appears below. The approach works on any host running an SMTP listener.

```python
import sys, smtplib

fromaddr = input("From: ")
toaddrs  = input("To: ").split(',')
print("Enter message, end with ^D:")
msg = ''
while True:
    line = sys.stdin.readline()
    if not line:
        break
    msg += line

# The actual mail send
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

```

There is also a Unix-only alternative that relies on sendmail. Where the sendmail program lives differs across systems; in some cases it's `/usr/lib/sendmail`, in others `/usr/sbin/sendmail`. Consult the sendmail manual page for guidance. Some sample code follows:

```python
import os

SENDMAIL = "/usr/sbin/sendmail"  # sendmail location
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write("To: receiver@example.com\n")
p.write("Subject: test\n")
p.write("\n")  # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
    print("Sendmail exit status", sts)

```

[Subject index](INDEX.md)
