# Python 3.14.0 beta 1 / library / heapq

[gh-110067](https://github.com/python/cpython/issues/110067): Promote the [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) max-heap helpers [`heapq.heapify_max()`](https://docs.python.org/3.14/library/heapq.html#heapq.heapify_max), [`heapq.heappush_max()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappush_max), [`heapq.heappop_max()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappop_max), and [`heapq.heapreplace_max()`](https://docs.python.org/3.14/library/heapq.html#heapq.heapreplace_max) to public status. The earlier underscored names remain for backwards compatibility. On top of that, the previously absent function [`heapq.heappushpop_max()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappushpop_max) was added across both the C and Python implementations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
