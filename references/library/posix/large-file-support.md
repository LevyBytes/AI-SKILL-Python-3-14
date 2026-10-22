# posix — Large File Support

### Large File Support

A number of operating systems (AIX and Solaris among them) can handle files exceeding 2 GiB even under a C programming model in which int and long are 32-bit. The usual trick is to declare the pertinent size and offset types as 64-bit. People sometimes call such files *large files*.

Python switches on large file support whenever an `off_t` is wider than a long and the long long is no smaller than an `off_t`. Turning this mode on may require configuring and building Python with particular compiler flags. On Solaris 2.6 and 2.7, for example, you would do roughly:

```python
CFLAGS="`getconf LFS_CFLAGS`" OPT="-g -O2 $CFLAGS" \
        ./configure

```

On Linux machines that handle large files, the following may do the job:

```python
CFLAGS='-D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64' OPT="-g -O2 $CFLAGS" \
        ./configure

```

[Subject index](INDEX.md) · [Previous](posix-the-most-common-posix-system-calls.md) · [Continue](posix-environ.md) · [Owning module, declaration or section: posix](posix-the-most-common-posix-system-calls.md)
