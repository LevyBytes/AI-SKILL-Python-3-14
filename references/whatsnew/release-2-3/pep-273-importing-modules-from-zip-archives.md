# What’s New in Python 2.3 / PEP 273: Importing Modules from ZIP Archives — zipimport

### PEP 273: Importing Modules from ZIP Archives

Loading modules from a ZIP-format archive becomes possible thanks to the new [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport) module. Importing it on your own is unnecessary; once a ZIP archive’s filename gets appended to `sys.path`, the import happens by itself. Here is an example:

```shell
amk@nyman:~/src/python$ unzip -l /tmp/example.zip
Archive:  /tmp/example.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  11-26-02 22:30   jwzthreading.py
 --------                   -------
     8467                   1 file
amk@nyman:~/src/python$ ./python
Python 2.3 (#1, Aug 1 2003, 19:54:32)
>>> import sys
>>> sys.path.insert(0, '/tmp/example.zip')  # Add .zip file to front of path
>>> import jwzthreading
>>> jwzthreading.__file__
'/tmp/example.zip/jwzthreading.py'
>>>

```

A ZIP archive’s filename is now allowed to be an entry within `sys.path`. While files of any sort may live in the ZIP archive, only those whose names match `*.py`, `*.pyc`, or `*.pyo` are importable. Should an archive carry nothing but `*.py` files, Python leaves the archive alone instead of writing the matching `*.pyc` file into it — which means importing can be fairly slow when a ZIP archive lacks `*.pyc` files.

You may also point at a path inside the archive so that importing draws solely from one subdirectory; the path `/tmp/example.zip/lib/`, for example, would import only out of the archive’s `lib/` subdirectory.

See also

[**PEP 273**](https://peps.python.org/pep-0273/) - Import Modules from Zip Archives

Authored by James C. Ahlstrom, who supplied an implementation as well. The specification laid out in [**PEP 273**](https://peps.python.org/pep-0273/) is what Python 2.3 adheres to, yet the implementation it actually relies on was authored by Just van Rossum and draws on the import hooks set out in [**PEP 302**](https://peps.python.org/pep-0302/). For an account of those new import hooks, consult the section PEP 302: New Import Hooks.

[Subject index](INDEX.md) · [Previous source section](pep-263-source-code-encodings.md) · [Next source section](pep-277-unicode-file-name-support-for-windows-nt.md) · [Release/subject declaration](standard-set-type.md)
