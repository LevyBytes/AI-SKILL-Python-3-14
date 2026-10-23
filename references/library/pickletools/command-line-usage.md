# pickletools - Command-line usage

### Command-line usage

Added in version 3.2.

Run from the shell, `python -m pickletools` takes apart whatever sits inside one or more pickle files. Keep in mind that to view the Python object held in the pickle, instead of the particulars of the pickle format, you'd likely reach for `-m pickle`. That said, should the pickle file you mean to inspect originate from an untrusted source, `-m pickletools` is the safer route, as it refrains from running any pickle bytecode.

To illustrate, suppose a tuple `(1, 2)` has been pickled into the file `x.pickle`:

```shell
$ python -m pickle x.pickle
(1, 2)

$ python -m pickletools x.pickle
    0: \x80 PROTO      3
    2: K    BININT1    1
    4: K    BININT1    2
    6: \x86 TUPLE2
    7: q    BINPUT     0
    9: .    STOP
highest protocol among opcodes = 2

```

[Subject index](INDEX.md) · [Previous](pickletools-tools-for-pickle-developers.md) · [Continue](command-line-options.md) · [Owning module, declaration or section: pickletools](pickletools-tools-for-pickle-developers.md)
