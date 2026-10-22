# pydoc — `pydoc` — Documentation generator and online help system

## pydoc — Documentation generator and online help system??

### `pydoc` — Documentation generator and online help system

**Source code:** [Lib/pydoc.py](https://github.com/python/cpython/tree/3.14/Lib/pydoc.py)

---

The `pydoc` module turns out documentation from Python modules automatically. That documentation can show up as pages of text on the console, get served to a web browser, or be saved to HTML files.

For modules, classes, functions and methods, the documentation displayed comes from the object's docstring (i.e. its [`__doc__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__doc__) attribute), and recursively from its documentable members. Lacking a docstring, `pydoc` attempts to lift a description from the run of comment lines positioned right ahead of where the class, function or method is defined inside the source file, or up at the module's top (see [`inspect.getcomments()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcomments)).

The built-in function [`help()`](https://docs.python.org/3.14/library/functions.html#help) fires up the online help system inside the interactive interpreter, which leans on `pydoc` to render its documentation as text on the console. You can likewise view that same text documentation from beyond the Python interpreter, by launching **pydoc** as a script at the command prompt of your operating system. To illustrate, running

```python
python -m pydoc sys

```

at a shell prompt brings up documentation covering the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module, styled much like the manual pages the Unix **man** command puts up. Whatever argument you hand **pydoc** can be a function name, a module, or a package, or a dotted reference pointing at a class, method, or function nested in a module or a module nested in a package. Should the argument to **pydoc** resemble a path (that is, it holds the path separator for your operating system, like a slash on Unix), and point at an existing Python source file, then documentation gets produced for that file.

Note

To track down objects and their documentation, `pydoc` imports the module(s) to be documented. As a result, any code at module level will run on that occasion. Reach for an `if __name__ == '__main__':` guard so that code runs only when a file is launched as a script and not merely imported.

While printing output to the console, **pydoc** tries to paginate the output for easier reading. Should either the `MANPAGER` or the `PAGER` environment variable be set, **pydoc** will take its value as a pagination program. With both set, `MANPAGER` wins.

Putting a `-w` flag in front of the argument makes HTML documentation get emitted into a file inside the current directory, in place of text appearing on the console.

Passing a `-k` flag ahead of the argument will hunt across the synopsis lines of every available module for the keyword handed as the argument, again much like the Unix **man** command. A module's synopsis line is the first line of its documentation string.

You can likewise reach for **pydoc** to stand up an HTTP server on your local machine, one that hands documentation to web browsers that visit. **python -m pydoc -p 1234** stands up a HTTP server on port 1234, letting you browse the documentation at `http://localhost:1234/` in your preferred web browser. Handing `0` as the port number picks an arbitrary unused port.

Warning

The `pydoc` HTTP server is meant for local use throughout development and isn't fit for production use.

**python -m pydoc -n &lt;hostname&gt;** will launch the server listening at the supplied hostname. The hostname defaults to "localhost" but should you want the server reachable from other machines, you may wish to change the host name the server answers to. Throughout development this proves especially handy if you want to run pydoc from inside a container.

**python -m pydoc -b** will launch the server and on top of that open a web browser onto a module index page. Every served page carries a navigation bar up top from which you may *Get* help on one individual item, *Search* across all modules bearing a keyword in their synopsis line, and head to the *Module index*, *Topics* and *Keywords* pages.

While **pydoc** turns out documentation, it leans on the current environment and path to track down modules. Hence, invoking **pydoc spam** documents exactly the version of the module you'd get were you to fire up the Python interpreter and type `import spam`.

Module docs for core modules are presumed to sit at `https://docs.python.org/X.Y/library/` in which `X` and `Y` stand for the interpreter's major and minor version numbers. Overriding this is a matter of pointing the `PYTHONDOCS` environment variable at a different URL or at a local directory that holds the Library Reference Manual pages.

Changed in version 3.2: Added the `-b` option.

Changed in version 3.3: The `-g` command line option was removed.

Changed in version 3.4: `pydoc` from now on leans on [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) in place of [`inspect.getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec) when pulling signature information out of callables.

Changed in version 3.7: Added the `-n` option.

[Subject index](INDEX.md)
