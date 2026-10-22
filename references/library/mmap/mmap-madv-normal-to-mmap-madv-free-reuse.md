# mmap — MADV_* Constants

### MADV_* Constants

 mmap.MADV_NORMAL

 mmap.MADV_RANDOM

 mmap.MADV_SEQUENTIAL

 mmap.MADV_WILLNEED

 mmap.MADV_DONTNEED

 mmap.MADV_REMOVE

 mmap.MADV_DONTFORK

 mmap.MADV_DOFORK

 mmap.MADV_HWPOISON

 mmap.MADV_MERGEABLE

 mmap.MADV_UNMERGEABLE

 mmap.MADV_SOFT_OFFLINE

 mmap.MADV_HUGEPAGE

 mmap.MADV_NOHUGEPAGE

 mmap.MADV_DONTDUMP

 mmap.MADV_DODUMP

 mmap.MADV_FREE

 mmap.MADV_NOSYNC

 mmap.MADV_AUTOSYNC

 mmap.MADV_NOCORE

 mmap.MADV_CORE

 mmap.MADV_PROTECT

 mmap.MADV_FREE_REUSABLE

 mmap.MADV_FREE_REUSE

Any of these options may be handed to `mmap.madvise()`. Not all of them exist on every system.

Availability: Systems with the madvise() system call.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](mmap-mmap-write-to-mmap-mmap-write-byte.md) · [Continue](mmap-map-shared-to-mmap-map-unix03.md) · [Owning module, declaration or section: mmap](mmap-mmap-class.md)
