# os — File Object Creation

### File Object Creation

These functions build new [file objects](https://docs.python.org/3.14/glossary.html#term-file-object). (See also `open()` for opening file descriptors.)

 os.fdopen(*fd*, **args*, ***kwargs*)

Give back an open file object bound to file descriptor *fd*. It aliases the [`open()`](https://docs.python.org/3.14/library/functions.html#open) built-in function and accepts identical arguments. The only difference: `fdopen()`'s first argument has to be an integer every time.

[Subject index](INDEX.md) · [Previous](os-clone-files-to-os-clone-vm.md) · [Continue](os-close-to-os-dup2.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
