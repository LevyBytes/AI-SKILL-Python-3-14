# `email`: Examples - Section introduction and initial examples

# Email.Examples

### [`email`](https://docs.python.org/3.14/library/email.html#module-email): Examples

Below are several examples showing how the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package can read, write, and send plain email messages along with richer MIME messages.

To begin, here is how a simple text message is built and sent (unicode characters are allowed in both the text body and the addresses):

```python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

```

The classes in the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) module make parsing [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) headers straightforward:

```python
# Import the email modules we'll need
#from email.parser import BytesParser
from email.parser import Parser
from email.policy import default

# If the e-mail headers are in a file, uncomment these two lines:
# with open(messagefile, 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)

#  Or for parsing headers in a string (this is an uncommon operation), use:
headers = Parser(policy=default).parsestr(
        'From: Foo Bar <user@example.com>\n'
        'To: <someone_else@example.com>\n'
        'Subject: Test message\n'
        '\n'
        'Body would go here\n')

#  Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers['to']))
print('From: {}'.format(headers['from']))
print('Subject: {}'.format(headers['subject']))

# You can also access the parts of the addresses:
print('Recipient username: {}'.format(headers['to'].addresses[0].username))
print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

```

The following demonstrates sending a MIME message carrying a set of family photos that might live in a directory:

[Subject index](INDEX.md) · [Continue](smtp-message-sending-example.md)
