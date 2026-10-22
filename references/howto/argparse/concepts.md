# Concepts

### Concepts

To preview the kind of behavior we'll dig into across this opening tutorial, let's lean on the **ls** command:

```shell
$ ls
cpython  devguide  prog.py  pypy  rm-unused-function.patch
$ ls pypy
ctypes_configure  demo  dotviewer  include  lib_pypy  lib-python ...
$ ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x  4 wena wena 4096 Feb  8 12:04 devguide
-rwxr-xr-x  1 wena wena  535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb  7 00:59 pypy
-rw-r--r--  1 wena wena  741 Feb 18 01:01 rm-unused-function.patch
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...

```

Those four commands teach us a handful of ideas:

- Even with no options supplied at all, the **ls** command does something handy. By default it prints out whatever the current directory holds.

- When we need more than the default behavior, we feed it extra detail. Here, we ask it to list a different directory, `pypy`. That move is called supplying a positional argument. The name fits because the program figures out how to handle the value purely from where that value sits on the command line. The idea is clearer with a command like **cp**, whose simplest form is `cp SRC DEST`. The first slot is *what you want copied,* and the second slot is *where you want it copied to*.

- Suppose now we want to alter how the program behaves. Here we print richer info per file rather than only the file names. In that situation the `-l` is referred to as an optional argument.

- That's a fragment of the help text. Its value is that you can run into a program you've never touched, and just by reading its help text you can work out how it operates.

[Subject index](INDEX.md) · [Previous source context](argparse-tutorial.md) · [Following source context](the-basics.md)
