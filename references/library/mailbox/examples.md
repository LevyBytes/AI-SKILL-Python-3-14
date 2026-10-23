# mailbox - Examples

### Examples

A short example that prints the subject of every message in a mailbox that looks worth a look:

```python
import mailbox
for message in mailbox.mbox('~/mbox'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'python' in subject.lower():
        print(subject)

```

To move every message out of a Babyl mailbox and into an MH mailbox, translating whatever format-specific details can in fact be translated:

```python
import mailbox
destination = mailbox.MH('~/Mail')
destination.lock()
for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))
destination.flush()
destination.unlock()

```

The example here distributes mail drawn from a handful of mailing lists across separate mailboxes, while taking pains to head off corruption from other programs writing at the same time, message loss should the program be interrupted, and an early exit caused by a malformed message inside the mailbox:

```python
import mailbox
import email.errors

list_names = ('python-list', 'python-dev', 'python-bugs')

boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}
inbox = mailbox.Maildir('~/Maildir', factory=None)

for key in inbox.iterkeys():
    try:
        message = inbox[key]
    except email.errors.MessageParseError:
        continue                # The message is malformed. Just leave it.

    for name in list_names:
        list_id = message['list-id']
        if list_id and name in list_id:
            # Get mailbox to use
            box = boxes[name]

            # Write copy to disk before removing original.
            # If there's a crash, you might duplicate a message, but
            # that's better than losing a message completely.
            box.lock()
            box.add(message)
            box.flush()
            box.unlock()

            # Remove original message
            inbox.lock()
            inbox.discard(key)
            inbox.flush()
            inbox.unlock()
            break               # Found destination, so stop looking.

for box in boxes.itervalues():
    box.close()

```

[Subject index](INDEX.md) · [Previous](mailbox-error-to-mailbox-formaterror.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
