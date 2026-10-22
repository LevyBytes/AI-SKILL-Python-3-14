# What’s New In Python 3.5 / zipapp — zipapp

### zipapp

The fresh [`zipapp`](https://docs.python.org/3.14/library/zipapp.html#module-zipapp) module (laid out in [**PEP 441**](https://peps.python.org/pep-0441/)) offers both an API and a command line tool for assembling executable Python Zip Applications; these landed back in Python 2.6 via [bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468), yet went largely unadvertised, whether then or afterward.

Using the fresh module, packaging your application reduces to gathering every file, a `__main__.py` file included, inside a directory `myapp` and then running:

```shell
$ python -m zipapp myapp
$ python myapp.pyz

```

Paul Moore supplied the module implementation in [bpo-23491](https://bugs.python.org/issue?@action=redirect&bpo=23491).

See also

[**PEP 441**](https://peps.python.org/pep-0441/) ? Improving Python ZIP Application Support

[Subject index](INDEX.md) · [Previous source section](typing.md) · [Next source section](argparse.md) · [Release/subject declaration](summary-release-highlights.md)
