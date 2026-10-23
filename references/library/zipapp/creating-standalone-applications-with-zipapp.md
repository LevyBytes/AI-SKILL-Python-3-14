# zipapp - Creating Standalone Applications with zipapp

### Creating Standalone Applications with zipapp

The `zipapp` module lets you put together self-contained Python programs, which you can then hand to end users who need nothing more than a fitting Python version installed. The trick is to fold every one of the application’s dependencies into the archive next to the application code itself.

Building a standalone archive goes like this:

1.

Lay out your application in a directory as you normally would, leaving you with a `myapp` directory that holds a `__main__.py` file along with any supporting application code.

2.

Pull all of the application’s dependencies into the `myapp` directory with pip:

```shell
$ python -m pip install -r requirements.txt --target myapp

```

(this presumes your project requirements live in a `requirements.txt` file — failing that, simply spell out the dependencies by hand on the pip command line).

3.

Wrap up the application with:

```shell
$ python -m zipapp -p "interpreter" myapp

```

Out of this comes a standalone executable runnable on any machine that has the right interpreter on hand. Consult Specifying the Interpreter for the particulars. You can ship it to users as one file.

Under Unix the `myapp.pyz` file is executable just as it is. Strip the `.pyz` extension by renaming the file if a “plain” command name suits you better. Under Windows the `myapp.pyz[w]` file is executable thanks to the Python interpreter registering the `.pyz` and `.pyzw` file extensions at install time.

[Subject index](INDEX.md) · [Previous](specifying-the-interpreter.md) · [Continue](caveats.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)
