# mmap - MAP_* Constants

### MAP_* Constants

 mmap.MAP_SHARED

 mmap.MAP_PRIVATE

 mmap.MAP_32BIT

 mmap.MAP_ALIGNED_SUPER

 mmap.MAP_ANON

 mmap.MAP_ANONYMOUS

 mmap.MAP_CONCEAL

 mmap.MAP_DENYWRITE

 mmap.MAP_EXECUTABLE

 mmap.MAP_HASSEMAPHORE

 mmap.MAP_JIT

 mmap.MAP_NOCACHE

 mmap.MAP_NOEXTEND

 mmap.MAP_NORESERVE

 mmap.MAP_POPULATE

 mmap.MAP_RESILIENT_CODESIGN

 mmap.MAP_RESILIENT_MEDIA

 mmap.MAP_STACK

 mmap.MAP_TPRO

 mmap.MAP_TRANSLATED_ALLOW_EXECUTE

 mmap.MAP_UNIX03

These are the assorted flags you may hand to `mmap.mmap()`. `MAP_ALIGNED_SUPER` exists only on FreeBSD and `MAP_CONCEAL` only on OpenBSD. Be aware that certain options may be absent on certain systems.

Changed in version 3.10: Added `MAP_POPULATE` constant.

Added in version 3.11: Added `MAP_STACK` constant.

Added in version 3.12: Added `MAP_ALIGNED_SUPER` and `MAP_CONCEAL` constants.

Added in version 3.13: Added `MAP_32BIT`, `MAP_HASSEMAPHORE`, `MAP_JIT`, `MAP_NOCACHE`, `MAP_NOEXTEND`, `MAP_NORESERVE`, `MAP_RESILIENT_CODESIGN`, `MAP_RESILIENT_MEDIA`, `MAP_TPRO`, `MAP_TRANSLATED_ALLOW_EXECUTE`, and `MAP_UNIX03` constants.

[Subject index](INDEX.md) · [Previous](mmap-madv-normal-to-mmap-madv-free-reuse.md) · [Continue](../modulefinder/modulefinder-addpackagepath-to-modulefinder-replacepackage.md) · [Owning module, declaration or section: mmap](mmap-mmap-class.md)
