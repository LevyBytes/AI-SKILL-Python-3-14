# SystemTap Tapsets

### SystemTap Tapsets

At a higher level, you engage the SystemTap integration through a “tapset” — the SystemTap counterpart to a library, which conceals a portion of the static markers’ low-level mechanics.

What follows is a tapset file built around a non-shared CPython build:

```none
/*
   Provide a higher-level wrapping around the function__entry and
   function__return markers:
 \*/
probe python.function.entry = process("python").mark("function__entry")
{
    filename = user_string($arg1);
    funcname = user_string($arg2);
    lineno = $arg3;
    frameptr = $arg4
}
probe python.function.return = process("python").mark("function__return")
{
    filename = user_string($arg1);
    funcname = user_string($arg2);
    lineno = $arg3;
    frameptr = $arg4
}

```

Once you place this file in SystemTap’s tapset directory (for instance `/usr/share/systemtap/tapset`), the following extra probepoints come into play:

 python.function.entry(str filename, str funcname, int lineno, frameptr)

This probe point signals that a Python function has started running. It fires solely for pure-Python (bytecode) functions.

 python.function.return(str filename, str funcname, int lineno, frameptr)

Acting as the opposite of `python.function.return`, this probe point reports that a Python function has finished (whether through `return` or because an exception was raised). It fires solely for pure-Python (bytecode) functions.

[Subject index](INDEX.md) · [Previous source context](c-probing-checks.md) · [Following source context](examples.md)
