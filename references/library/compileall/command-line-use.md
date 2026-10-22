# compileall — Command-line use

### Command-line use

You can also invoke this module from the command line (via **python -m compileall**) to byte-compile Python sources.

 directory ...

 file ...

The positional arguments name either files to compile or directories holding source files, which are walked recursively. When nothing is supplied, the tool acts as though it had received `-l *<directories from sys.path>*`.

 -l

Stay at the top level — compile only the source files sitting directly in the named (or implied) directories, without descending into subdirectories.

 -f

Rebuild unconditionally, even when the timestamps already look current.

 -q

Suppress the listing of compiled files. Given a single time, error messages are still shown. Given twice (`-qq`), every bit of output goes away.

 -d destdir

A directory placed ahead of the path of each compiled file. It surfaces in compilation-time tracebacks and is also baked into the byte-code file, where it serves tracebacks and other messages whenever the source file is missing at the moment the byte-code runs.

 -s strip_prefix

Drop the supplied prefix from the paths stored inside the `.pyc` files, making those paths relative to it.

This option can be used with `-p` but not with `-d`.

 -p prepend_prefix

Add the supplied prefix to the front of the paths stored inside the `.pyc` files. Pass `-p /` to render the paths absolute.

This option can be used with `-s` but not with `-d`.

 -x regex

The full path of every file in line for compilation is searched with regex, and any file producing a match is left out.

 -i list

Open the file `list` and append every line it holds to the set of files and directories to be compiled. When `list` is `-`, the lines come from `stdin`.

 -b

Emit the byte-code files at their legacy paths and names, which can clobber byte-code files produced by a different Python release. By default the files land at their [**PEP 3147**](https://peps.python.org/pep-3147/) paths and names, letting byte-code from several Python versions live side by side.

 -r

Set the deepest recursion level reached in subdirectories. Supplying it causes the `-l` option to be ignored. As an illustration, **python -m compileall &lt;directory&gt; -r 0** behaves the same way as **python -m compileall &lt;directory&gt; -l**.

 -j N

Spread compilation of the files within the directory across *N* workers. When `0` is supplied, the value returned by [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) is used instead.

 --invalidation-mode [timestamp|checked-hash|unchecked-hash]

Decide how the produced byte-code files get invalidated while running. With the `timestamp` value, `.pyc` files carrying the source timestamp and size are produced. The `checked-hash` and `unchecked-hash` values instead yield hash-based pycs, which store a hash of the source file's contents in place of a timestamp. Refer to [Cached bytecode invalidation](https://docs.python.org/3.14/reference/import.html#pyc-invalidation) for the details of how Python checks bytecode cache files while running. The fallback is `timestamp` when the `SOURCE_DATE_EPOCH` environment variable is unset, and `checked-hash` once the `SOURCE_DATE_EPOCH` environment variable is present.

 -o level

Compile at the supplied optimization level. Repeat it to build several levels in a single run (for instance, `compileall -o 1 -o 2`).

 -e dir

Skip symlinks that lead outside the supplied directory.

 --hardlink-dupes

When two `.pyc` files at differing optimization levels turn out identical, link them with hard links to merge the duplicates.

Changed in version 3.2: Added the `-i`, `-b` and `-h` options.

Changed in version 3.5: Introduced the `-j`, `-r`, and `-qq` options. The `-q` option became a multilevel value. From now on `-b` invariably emits a byte-code file whose extension is `.pyc`, and never `.pyo`.

Changed in version 3.7: Added the `--invalidation-mode` option.

Changed in version 3.9: Introduced the `-s`, `-p`, `-e` and `--hardlink-dupes` options. Lifted the default recursion ceiling from 10 up to [`sys.getrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit). Made it possible to give the `-o` option more than once.

No command-line switch governs the optimization level applied by the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function, since the Python interpreter itself already offers one: **python -O -m compileall**.

In the same way, the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function honors the [`sys.pycache_prefix`](https://docs.python.org/3.14/library/sys.html#sys.pycache_prefix) setting. The resulting bytecode cache pays off only when `compile()` runs under the same `sys.pycache_prefix` (if any) that will apply at runtime.

[Subject index](INDEX.md) · [Previous](compileall-byte-compile-python-libraries.md) · [Continue](compileall-compile-dir-to-compileall-compile-file.md) · [Owning module, declaration or section: compileall](compileall-byte-compile-python-libraries.md)
