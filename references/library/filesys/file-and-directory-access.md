# fileinput - File and Directory Access

## File and Directory Access

### File and Directory Access

What this chapter's modules concern themselves with is disk files and directories. Among them, for instance, you'll find modules for inspecting file properties, working with paths in a cross-platform fashion, and spinning up temporary files. Here is the complete roster of modules covered:

- [`pathlib` - Object-oriented filesystem paths](https://docs.python.org/3.14/library/pathlib.html)
  - [Basic use](https://docs.python.org/3.14/library/pathlib.html#basic-use)
  - [Exceptions](https://docs.python.org/3.14/library/pathlib.html#exceptions)
  - [Pure paths](https://docs.python.org/3.14/library/pathlib.html#pure-paths)
    - [General properties](https://docs.python.org/3.14/library/pathlib.html#general-properties)
    - [Operators](https://docs.python.org/3.14/library/pathlib.html#operators)
    - [Accessing individual parts](https://docs.python.org/3.14/library/pathlib.html#accessing-individual-parts)
    - [Methods and properties](https://docs.python.org/3.14/library/pathlib.html#methods-and-properties)

  - [Concrete paths](https://docs.python.org/3.14/library/pathlib.html#concrete-paths)
    - [Parsing and generating URIs](https://docs.python.org/3.14/library/pathlib.html#parsing-and-generating-uris)
    - [Expanding and resolving paths](https://docs.python.org/3.14/library/pathlib.html#expanding-and-resolving-paths)
    - [Querying file type and status](https://docs.python.org/3.14/library/pathlib.html#querying-file-type-and-status)
    - [Reading and writing files](https://docs.python.org/3.14/library/pathlib.html#reading-and-writing-files)
    - [Reading directories](https://docs.python.org/3.14/library/pathlib.html#reading-directories)
    - [Creating files and directories](https://docs.python.org/3.14/library/pathlib.html#creating-files-and-directories)
    - [Copying, moving and deleting](https://docs.python.org/3.14/library/pathlib.html#copying-moving-and-deleting)
    - [Permissions and ownership](https://docs.python.org/3.14/library/pathlib.html#permissions-and-ownership)

  - [Pattern language](https://docs.python.org/3.14/library/pathlib.html#pattern-language)
  - [Comparison to the `glob` module](https://docs.python.org/3.14/library/pathlib.html#comparison-to-the-glob-module)
  - [Comparison to the `os` and `os.path` modules](https://docs.python.org/3.14/library/pathlib.html#comparison-to-the-os-and-os-path-modules)
    - [Corresponding tools](https://docs.python.org/3.14/library/pathlib.html#corresponding-tools)

  - [Protocols](https://docs.python.org/3.14/library/pathlib.html#module-pathlib.types)

- [`os.path` - Common pathname manipulations](https://docs.python.org/3.14/library/os.path.html)
- [`stat` - Interpreting `stat()` results](https://docs.python.org/3.14/library/stat.html)
- [`filecmp` - File and Directory Comparisons](https://docs.python.org/3.14/library/filecmp.html)
  - [The `dircmp` class](https://docs.python.org/3.14/library/filecmp.html#the-dircmp-class)

- [`tempfile` - Generate temporary files and directories](https://docs.python.org/3.14/library/tempfile.html)
  - [Examples](https://docs.python.org/3.14/library/tempfile.html#examples)
  - [Deprecated functions and variables](https://docs.python.org/3.14/library/tempfile.html#deprecated-functions-and-variables)

- [`glob` - Unix style pathname pattern expansion](https://docs.python.org/3.14/library/glob.html)
  - [Examples](https://docs.python.org/3.14/library/glob.html#examples)

- [`fnmatch` - Unix filename pattern matching](https://docs.python.org/3.14/library/fnmatch.html)
- [`linecache` - Random access to text lines](https://docs.python.org/3.14/library/linecache.html)
- [`shutil` - High-level file operations](https://docs.python.org/3.14/library/shutil.html)
  - [Directory and files operations](https://docs.python.org/3.14/library/shutil.html#directory-and-files-operations)
    - [Platform-dependent efficient copy operations](https://docs.python.org/3.14/library/shutil.html#platform-dependent-efficient-copy-operations)
    - [copytree example](https://docs.python.org/3.14/library/shutil.html#copytree-example)
    - [rmtree example](https://docs.python.org/3.14/library/shutil.html#rmtree-example)

  - [Archiving operations](https://docs.python.org/3.14/library/shutil.html#archiving-operations)
    - [Archiving example](https://docs.python.org/3.14/library/shutil.html#archiving-example)
    - [Archiving example with *base_dir*](https://docs.python.org/3.14/library/shutil.html#archiving-example-with-base-dir)

  - [Querying the size of the output terminal](https://docs.python.org/3.14/library/shutil.html#querying-the-size-of-the-output-terminal)

See also

Module [`os`](https://docs.python.org/3.14/library/os.html#module-os)

Interfaces to the operating system, among them functions for handling files at a level beneath Python's own [file objects](https://docs.python.org/3.14/glossary.html#term-file-object).

Module [`io`](https://docs.python.org/3.14/library/io.html#module-io)

The I/O library that ships with Python, bringing together abstract classes alongside concrete ones like file I/O.

Built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open)

Python's go-to means of opening files to read from and write to them.

[Subject index](INDEX.md)
