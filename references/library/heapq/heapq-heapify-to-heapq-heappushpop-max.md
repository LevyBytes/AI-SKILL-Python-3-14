# heapq: `heapq.heapify()`, `heapq.heappush()`, `heapq.heappop()`, `heapq.heappushpop()`, `heapq.heapreplace()`, `heapq.heapify_max()`, `heapq.heappush_max()`, `heapq.heappop_max()`, `heapq.heappushpop_max()`

### `heapq` — Heap queue algorithm

**Source code:** [Lib/heapq.py](https://github.com/python/cpython/tree/3.14/Lib/heapq.py)

---

The heap queue algorithm — equivalently called the priority queue algorithm — is implemented by this module.

A min-heap is a binary tree in which the value held by each parent node is no greater than the values held by either of its children. That property is what we call the heap invariant.

This implementation backs min-heaps with lists satisfying `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for every *k* where the compared entries are present. Indexing starts at zero. What makes a min-heap notable is that the root, `heap[0]`, is always the smallest element.

A max-heap obeys the opposite invariant: each parent node holds a value *greater* than either child. The backing lists here satisfy `maxheap[2*k+1] <= maxheap[k]` and `maxheap[2*k+2] <= maxheap[k]` for every *k* where the compared entries exist. Now the root, `maxheap[0]`, holds the *largest* element, and `heap.sort(reverse=True)` keeps the max-heap invariant intact.

In two ways the `heapq` API parts company with the heap algorithms found in textbooks: (a) Indexing here begins at zero. That choice makes the link between a node's index and the indexes of its children a touch harder to read, yet it fits better because Python itself indexes from zero. (b) Because max-heaps lend themselves to in-place sorting, textbooks tend to emphasize them. Our code prefers min-heaps instead, since they map more naturally onto Python [`lists`](https://docs.python.org/3.14/library/stdtypes.html#list).

Together those choices let you treat the heap as an ordinary Python list with no nasty surprises: `heap[0]` holds the smallest entry, and `heap.sort()` keeps the heap invariant intact!

Just as [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) does, this code relies solely on the `<` operator when comparing, whether the structure is a min-heap or a max-heap.

Throughout the API listed below, and across this document, when *heap* appears on its own it normally means a min-heap. Max-heap entries in the API carry a `_max` suffix in their names.

You can build a heap from a list set to `[]`, or convert an existing list into a min-heap or a max-heap by calling the `heapify()` or `heapify_max()` functions, in that order.

These functions apply to min-heaps:

 heapq.heapify(*x*)

Transform list *x* into a min-heap, in-place, in linear time.

 heapq.heappush(*heap*, *item*)

Add the value *item* to the *heap* while keeping the min-heap invariant in place.

 heapq.heappop(*heap*)

Remove the smallest entry from the *heap*, return it, and keep the min-heap invariant intact. An empty heap triggers [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError). Read `heap[0]` to look at the smallest entry without removing it.

 heapq.heappushpop(*heap*, *item*)

Push *item* onto the heap, then pop the smallest entry off the *heap* and return it. Running both as one operation is faster than calling `heappush()` and then making a separate `heappop()` call.

 heapq.heapreplace(*heap*, *item*)

Remove the smallest entry from the *heap* and return it, while also adding the new *item*. The heap's size stays the same. An empty heap triggers [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

Doing this as a single operation beats a `heappop()` paired with a `heappush()`, and it can suit a heap of fixed size better. This pop-then-push pairing always hands back an entry already in the heap, swapping in *item* in its place.

The returned value can exceed the *item* you supplied. When that isn't what you want, reach for `heappushpop()` instead. That push-then-pop pairing returns whichever of the two values is smaller and keeps the larger one in the heap.

For max-heaps, the following functions are provided:

 heapq.heapify_max(*x*)

Transform list *x* into a max-heap, in-place, in linear time.

Added in version 3.14.

 heapq.heappush_max(*heap*, *item*)

Add the value *item* to the max-heap *heap* while keeping the max-heap invariant in place.

Added in version 3.14.

 heapq.heappop_max(*heap*)

Remove the largest entry from the max-heap *heap*, return it, and keep the max-heap invariant intact. An empty max-heap triggers [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError). Read `maxheap[0]` to look at the largest entry without removing it.

Added in version 3.14.

 heapq.heappushpop_max(*heap*, *item*)

Push *item* onto the max-heap *heap*, then pop the largest entry off *heap* and return it. Running both as one operation is faster than calling `heappush_max()` and then making a separate `heappop_max()` call.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](heap-queue-algorithm.md) · [Continue](heapq-heapreplace-max-to-heapq-nsmallest.md)
