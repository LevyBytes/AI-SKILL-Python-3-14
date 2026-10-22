# 4.1.6. Offline installs

### 4.1.6. Offline installs

To carry out offline installs of Python, you first have to build an offline index on a machine that does have network access.

```none
$> py install --download=<PATH> ... <TAG>...

```

The `--download=<PATH>` option fetches the packages for the named tags and builds a directory holding them plus an `index.json` file fit for installation later on. You can move that whole directory to the offline machine and use it to install one or more of the bundled runtimes:

```none
$> py install --source="<PATH>\index.json" <TAG>...

```

You can install the Python install manager by downloading its installer and relocating it to another machine before installation.

As an alternative, the ZIP files within an offline index directory can simply be carried to another machine and unpacked. That registers the install in no way, so it has to be launched by referencing the executables in the extracted directory directly, yet it is occasionally the preferable route when installing the Python install manager is not possible or convenient.

By these means, Python runtimes can be installed and managed on a machine that has no internet access.

[Subject index](INDEX.md) · [Previous source section](installing-runtimes.md) · [Following source section](uninstalling-runtimes.md)
