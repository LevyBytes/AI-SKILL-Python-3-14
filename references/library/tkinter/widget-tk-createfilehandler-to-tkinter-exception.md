# tkinter — File Handlers

### File Handlers

Tk lets you register, and later unregister, a callback function that the Tk mainloop invokes once I/O becomes possible on a file descriptor. Each file descriptor may hold just one handler. Sample code:

```python
import tkinter
widget = tkinter.Tk()
mask = tkinter.READABLE | tkinter.WRITABLE
widget.tk.createfilehandler(file, mask, callback)
...
widget.tk.deletefilehandler(file)

```

Windows does not offer this feature.

Because the count of bytes ready to read is unknown to you, you’ll probably want to steer clear of the [`BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) or [`TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) or [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) methods, since each insists on reading a fixed number of bytes. With sockets, the [`recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv) or [`recvfrom()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvfrom) methods serve nicely; for other files, fall back on raw reads or `os.read(file.fileno(), maxbytecount)`.

 Widget.tk.createfilehandler(*file*, *mask*, *func*)

Registers *func* as the file handler callback function. For the *file* argument you may pass either an object sporting a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method (a file or socket object, say) or an integer file descriptor. The *mask* argument is any of the three constants below OR-ed together. Here is how the callback gets invoked:

```python
callback(file, mask)

```

 Widget.tk.deletefilehandler(*file*)

Removes the registration of a file handler.

 _tkinter.READABLE

 _tkinter.WRITABLE

 _tkinter.EXCEPTION

The constants you place in the *mask* arguments.

[Subject index](INDEX.md) · [Previous](images.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
