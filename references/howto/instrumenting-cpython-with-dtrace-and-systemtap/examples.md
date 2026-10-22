# Examples

### Examples

Drawing on the tapset shown above, this SystemTap script realizes the earlier example of tracing Python’s function-call hierarchy in a tidier way, with no need to reference the static markers by name:

```none
probe python.function.entry
{
  printf("%s => %s in %s:%d\n",
         thread_indent(1), funcname, filename, lineno);
}

probe python.function.return
{
  printf("%s <= %s in %s:%d\n",
         thread_indent(-1), funcname, filename, lineno);
}

```

Relying on that same tapset, the script below offers a top-like display of every executing CPython frame, surfacing the 20 most often entered bytecode frames once per second across the entire system:

```none
global fn_calls;

probe python.function.entry
{
    fn_calls[pid(), filename, funcname, lineno] += 1;
}

probe timer.ms(1000) {
    printf("\033[2J\033[1;1H") /* clear screen \*/
    printf("%6s %80s %6s %30s %6s\n",
           "PID", "FILENAME", "LINE", "FUNCTION", "CALLS")
    foreach ([pid, filename, funcname, lineno] in fn_calls- limit 20) {
        printf("%6d %80s %6d %30s %6d\n",
            pid, filename, lineno, funcname,
            fn_calls[pid, filename, funcname, lineno]);
    }
    delete fn_calls;
}

```

[Subject index](INDEX.md) · [Previous source context](systemtap-tapsets.md)
