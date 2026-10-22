# heapq — Theory

### Theory

A heap is an array satisfying `a[k] <= a[2*k+1]` and `a[k] <= a[2*k+2]` for every *k*, with elements counted from 0. For comparison purposes, any missing element is treated as infinite. What makes a heap notable is that `a[0]` is forever its smallest element.

That odd-looking invariant is intended to give an efficient in-memory layout for a tournament. The values shown below are *k* rather than `a[k]`:

```python
                               0

              1                                 2

      3               4                5               6

  7       8       9       10      11      12      13      14

15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

```

Within the tree drawn above, each cell *k* sits over `2*k+1` and `2*k+2`. In the ordinary knockout brackets you'd see in sports, each cell is whichever of the two cells beneath it won, and you can follow a winner down the tree to recover every opponent they faced. Yet for many computer uses of these tournaments, recovering a winner's history isn't needed. To save memory, once a winner advances we attempt to fill its spot with something from a lower level, and the rule shifts to: a cell together with the two cells beneath it holds three distinct items, while the top cell “wins” against the two below it.

So long as this heap invariant is upheld at every moment, index 0 is plainly the outright winner. The most straightforward algorithm to drop it and locate the “next” winner is to lift some loser (cell 30 in the diagram above, say) into position 0, then let that new 0 percolate down the tree, swapping values along the way, until the invariant is restored. That is plainly logarithmic in the tree's total item count. Looping across every item yields an *O*(*n* log *n*) sort.

A pleasant trait of this sort is that you can insert fresh items efficiently while it's still running, as long as those items aren't “better” than the most recent 0’th element you pulled out. That proves especially handy in simulation work, where the tree carries all pending events and the “win” condition picks out the smallest scheduled time. Whenever an event queues other events to run, those land in the future, so dropping them into the heap is easy. That makes a heap a fine structure for building schedulers (which is exactly what I used for my MIDI sequencer :-).

People have studied a range of structures for building schedulers, and heaps suit the job well: they're reasonably fast, that speed stays nearly constant, and their worst case isn't far off their average. Other representations do beat them overall, though their worst cases can be dreadful.

Heaps also shine in large on-disk sorts. As you very likely already know, a big sort means generating “runs” (pre-sorted sequences whose length usually tracks the available CPU memory), then merging those runs across several passes, and that merging is frequently arranged very shrewdly [1]. Getting the initial sort to yield the longest possible runs matters a great deal. Tournaments serve that goal nicely. If you commit all available memory to holding a tournament and replace-and-percolate the items that still belong in the current run, you'll get runs twice the size of memory for random input, and far longer for input that's loosely ordered.

What's more, when you write the 0’th item out to disk and read in an input that may no longer fit the current tournament (because its value “wins” over the value just emitted), it can't stay in the heap, so the heap shrinks. That freed memory can be reused right away to start building a second heap, which grows at precisely the pace the first one is shrinking. The moment the first heap is gone, you swap heaps and begin a fresh run. Clever and quite effective!

In short, heaps are handy memory structures worth knowing. I reach for them in a handful of applications, and I reckon it's worth keeping a ‘heap’ module on hand. :-)

Footnotes

[Subject index](INDEX.md) · [Previous](priority-queue-implementation-notes.md) · [Continue](../hmac/hmac-new-to-hmac-digest.md) · [Owning module, declaration or section: heapq](heapq-heapify-to-heapq-heappushpop-max.md)
