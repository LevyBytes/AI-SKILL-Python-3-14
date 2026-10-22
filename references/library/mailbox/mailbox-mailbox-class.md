# mailbox: `mailbox.Mailbox`

### `Mailbox` objects

 *class *mailbox.Mailbox

A mailbox, open to inspection and modification.

The `Mailbox` class lays out an interface and isn't meant to be instantiated. Rather, format-specific subclasses should derive from `Mailbox`, and your code should instantiate one particular subclass.

The `Mailbox` interface resembles a dictionary, with small keys standing for messages. Keys are handed out by the `Mailbox` instance they'll be used with and carry meaning only to that `Mailbox` instance. A key keeps identifying a message even when the matching message is altered, for example by being swapped out for another message.

You can add messages to a `Mailbox` instance via the set-like method `add()` and take them away via a `del` statement or the set-like methods `remove()` and `discard()`.

In a few notable respects, `Mailbox` interface semantics part ways with dictionary semantics. On every request for a message, a fresh representation (usually a `Message` instance) is produced from the mailbox's current state. In the same way, when a message is added to a `Mailbox` instance, the contents of the supplied message representation are copied. In neither situation does the `Mailbox` instance retain a reference to the message representation.

The default `Mailbox` [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) walks over message representations rather than keys, which is what the default [`dictionary`](https://docs.python.org/3.14/library/stdtypes.html#dict) iterator walks over. Furthermore, altering a mailbox while iterating is safe and well-defined. An iterator won't see messages added to the mailbox after that iterator was created. Messages taken out of the mailbox before the iterator reaches them will be silently passed over, though using a key obtained from an iterator may yield a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should the matching message be removed afterward.

Warning

Exercise great care when altering mailboxes that another process might be changing at the same time. The safest mailbox format for such work is `Maildir`; steer clear of single-file formats like `mbox` for concurrent writing. When you alter a mailbox, you *must* lock it by invoking the `lock()` and `unlock()` methods *before* you read any messages from the file or apply any change through adding or deleting a message. Neglecting to lock the mailbox risks losing messages or corrupting the whole mailbox.

`Mailbox` instances have the following methods:

[Subject index](INDEX.md) · [Previous](mailbox-manipulate-mailboxes-in-various-formats.md) · [Continue](mailbox-mailbox-add-to-mailbox-mailbox-get-file.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
