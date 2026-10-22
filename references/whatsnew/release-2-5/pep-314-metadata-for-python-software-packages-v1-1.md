# What's New in Python 2.5 / PEP 314: Metadata for Python Software Packages v1.1

### PEP 314: Metadata for Python Software Packages v1.1

Distutils picked up some basic support for dependencies. The `setup()` function now takes the `requires`, `provides`, and `obsoletes` keyword parameters. Building a source distribution with the `sdist` command will record the dependency details into the `PKG-INFO` file.

There is also a new `download_url` keyword parameter, which you should point at a URL holding the package's source code. As a result, it's now feasible to find an entry within the package index, work out which dependencies a package has, and fetch the packages it needs.

```python
VERSION = '1.0'
setup(name='PyPackage',
      version=VERSION,
      requires=['numarray', 'zlib (>=1.1.4)'],
      obsoletes=['OldPackage']
      download_url=('http://www.example.com/pypackage/dist/pkg-%s.tar.gz'
                    % VERSION),
     )

```

A further improvement to the Python package index over at [https://pypi.org](https://pypi.org) is that it keeps both source and binary archives for a package. To send a package up to the repository you use the new **upload** Distutils command.

Uploading a package requires that you first be able to assemble a distribution via the **sdist** Distutils command. After that succeeds, running `python setup.py upload` adds your package into the PyPI archive. If you like, you may GPG-sign the package by passing along the `--sign` and `--identity` options.

Package uploading was implemented by Martin von Löwis and Richard Jones.

See also

[**PEP 314**](https://peps.python.org/pep-0314/) - Metadata for Python Software Packages v1.1

This PEP was proposed and authored by A.M. Kuchling, Richard Jones, and Fred Drake; its implementation came from Richard Jones and Fred Drake.

[Subject index](INDEX.md) · [Previous source section](pep-309-partial-function-application.md) · [Next source section](pep-328-absolute-and-relative-imports.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
