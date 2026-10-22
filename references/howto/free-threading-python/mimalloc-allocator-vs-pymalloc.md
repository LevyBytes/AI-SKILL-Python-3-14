# mimalloc allocator vs pymalloc

#### mimalloc allocator vs pymalloc

For small requests of 512 bytes or under, the standard build typically reaches for the “pymalloc” memory allocator. The free-threaded build skips pymalloc entirely and routes every Python object through the “mimalloc” allocator. Several traits of pymalloc keep memory footprint down: little overhead per allocated block, solid protection against fragmentation, and prompt handing of free memory back to the operating system. While mimalloc holds up well on those fronts too, it can carry somewhat more overhead.

Under the free-threaded build, mimalloc spreads memory across several distinct heaps — four at present. Every GC-supporting object, for instance, draws from a dedicated heap. Because the heaps are separate, free space sitting in one heap can't serve an allocation aimed at a different heap. On top of that, certain heaps are set up to apply QSBR (quiescent-state based reclamation) when reclaiming the memory underpinning the heap — referred to as “pages” in mimalloc's vocabulary. Relying on QSBR introduces a gap between the moment all of a page's memory blocks are freed and the moment that page is actually released, whether for fresh allocations or back to the OS.

mimalloc likewise puts off handing freed memory back to the OS. Shorten that wait by setting the `MIMALLOC_PURGE_DELAY` environment variable to `0`, though doing so will probably cost the allocator some performance.

[Subject index](INDEX.md) · [Previous source context](qsbr-can-delay-freeing-of-memory.md) · [Following source context](free-threaded-reference-counting-and-lifetimes.md)
