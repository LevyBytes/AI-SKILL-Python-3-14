# Static SystemTap markers

### Static SystemTap markers

At the lowest level, working with the SystemTap integration means referencing the static markers yourself. Doing so obliges you to name, explicitly, the binary file that holds them.

As an example, the SystemTap script below can render the call/return hierarchy for a Python script:

```none
probe process("python").mark("function__entry") {
     filename = user_string($arg1);
     funcname = user_string($arg2);
     lineno = $arg3;

     printf("%s => %s in %s:%d\\n",
            thread_indent(1), funcname, filename, lineno);
}

probe process("python").mark("function__return") {
    filename = user_string($arg1);
    funcname = user_string($arg2);
    lineno = $arg3;

    printf("%s <= %s in %s:%d\\n",
           thread_indent(-1), funcname, filename, lineno);
}

```

You launch it like so:

```shell
$ stap \
  show-call-hierarchy.stp \
  -c "./python test.py"

```

The resulting output reads as follows:

```none
11408 python(8274):        => __contains__ in Lib/_abcoll.py:362
11414 python(8274):         => __getitem__ in Lib/os.py:425
11418 python(8274):          => encode in Lib/os.py:490
11424 python(8274):          <= encode in Lib/os.py:493
11428 python(8274):         <= __getitem__ in Lib/os.py:426
11433 python(8274):        <= __contains__ in Lib/_abcoll.py:366

```

in which the columns hold:

- elapsed microseconds counted from when the script began

- the executable's name

- the process PID

while everything after that traces the call/return hierarchy while the script runs.

When CPython is compiled as a [`--enable-shared`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-shared) build, the markers live inside the libpython shared library, so the probe’s dotted path has to account for that. As an instance, take this line drawn from the earlier sample:

```none
probe process("python").mark("function__entry") {

```

would have to become:

```none
probe process("python").library("libpython3.6dm.so.1.0").mark("function__entry") {

```

(taking CPython 3.6 compiled as a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build))

[Subject index](INDEX.md) · [Previous source context](static-dtrace-probes.md) · [Following source context](available-static-markers.md)
