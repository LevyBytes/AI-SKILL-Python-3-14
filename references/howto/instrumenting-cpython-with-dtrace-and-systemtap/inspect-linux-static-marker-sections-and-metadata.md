# Inspect Linux static-marker sections and metadata

Under Linux, you can confirm whether the SystemTap static markers made it into the compiled binary by checking for the presence of a “.note.stapsdt” section.

```shell
$ readelf -S ./python | grep .note.stapsdt
[30] .note.stapsdt        NOTE         0000000000000000 00308d78

```

When Python was compiled into a shared library (using the [`--enable-shared`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-shared) configure option), you must search inside that shared library instead. As an illustration:

```shell
$ readelf -S libpython3.3dm.so.1.0 | grep .note.stapsdt
[29] .note.stapsdt        NOTE         0000000000000000 00365b68

```

A recent enough readelf is able to dump the metadata:

```shell
$ readelf -n ./python

Displaying notes found at file offset 0x00000254 with length 0x00000020:
    Owner                 Data size          Description
    GNU                  0x00000010          NT_GNU_ABI_TAG (ABI version tag)
        OS: Linux, ABI: 2.6.32

Displaying notes found at file offset 0x00000274 with length 0x00000024:
    Owner                 Data size          Description
    GNU                  0x00000014          NT_GNU_BUILD_ID (unique build ID bitstring)
        Build ID: df924a2b08a7e89f6e11251d4602022977af2670

Displaying notes found at file offset 0x002d6c30 with length 0x00000144:
    Owner                 Data size          Description
    stapsdt              0x00000031          NT_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: gc__start
        Location: 0x00000000004371c3, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bf6
        Arguments: -4@%ebx
    stapsdt              0x00000030          NT_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: gc__done
        Location: 0x00000000004374e1, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bf8
        Arguments: -8@%rax
    stapsdt              0x00000045          NT_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: function__entry
        Location: 0x000000000053db6c, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6be8
        Arguments: 8@%rbp 8@%r12 -4@%eax
    stapsdt              0x00000046          NT_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: function__return
        Location: 0x000000000053dba8, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bea
        Arguments: 8@%rbp 8@%r12 -4@%eax

```

That metadata shown above tells SystemTap how to rewrite carefully chosen machine-code instructions so that the tracing hooks a SystemTap script depends on become active.

[Subject index](INDEX.md) · [Build DTrace/SystemTap markers and inspect macOS probes](build-dtrace-systemtap-markers-and-inspect-macos-probes.md) · [Previous source context](build-dtrace-systemtap-markers-and-inspect-macos-probes.md) · [Following source context](static-dtrace-probes.md)
