# mailbox.MH: `list_folders()`, `get_folder()`, `add_folder()`, `remove_folder()`, `get_sequences()`, `set_sequences()`, `pack()`

list_folders()

Return a list of the names of all folders.

 get_folder(*folder*)

Return an `MH` instance standing for the folder whose name is *folder*. A `NoSuchMailboxError` exception is raised should the folder not exist.

 add_folder(*folder*)

Create a folder whose name is *folder* and return an `MH` instance standing for it.

 remove_folder(*folder*)

Delete the folder whose name is *folder*. Should the folder hold any messages, a `NotEmptyError` exception will be raised and the folder won't be deleted.

 get_sequences()

Return a dictionary mapping sequence names to key lists. Where there are no sequences, the empty dictionary comes back.

 set_sequences(*sequences*)

Re-define which sequences exist in the mailbox from *sequences*, a dictionary mapping names to key lists, like the one `get_sequences()` returns.

 pack()

Rename messages in the mailbox as needed to close gaps in numbering. Entries in the sequences list are updated to match.

Note

[Subject index](INDEX.md) · [Previous](mailbox-mh-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.MH](mailbox-mh-class.md) · [Owning module, declaration or section: `MH` objects](mailbox-mh-class.md) · [Required continuation of the source contract](remove-to-close.md)
