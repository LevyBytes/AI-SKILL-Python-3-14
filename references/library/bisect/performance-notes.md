# bisect — Performance Notes

### Performance Notes

As you write performance-critical code that draws on *bisect()* and *insort()*, hold these points in view:

- Where you need to search across ranges of values, bisection serves well; for pinning down individual values, dictionaries run faster.

- Running at *O*(*n*), the *insort()* functions get that way because the linear-time insertion step overshadows the logarithmic search step.

- Being stateless, the search functions throw away key function results once they've been used. As a result, calling the search functions inside a loop can have the key function fire over and over on the very same array elements. Should the key function be slow, think about wrapping it in [`functools.cache()`](https://docs.python.org/3.14/library/functools.html#functools.cache) so the work isn't repeated. Another option is to search an array of keys you've computed ahead of time to find the insertion point, as the examples section further down demonstrates.

See also

- [Sorted Collections](https://grantjenks.com/docs/sortedcollections/) is a high-performance module that relies on *bisect* to keep collections of data in sorted order.

- The [SortedCollection recipe](https://code.activestate.com/recipes/577197-sortedcollection/) leans on bisect to assemble a fully featured collection class offering easy-to-use search methods plus support for a key-function. Its keys are computed in advance, sparing needless calls to the key function while searches run.

[Subject index](INDEX.md) · [Previous](bisect-bisect-left-to-bisect-insort.md) · [Continue](searching-sorted-lists.md) · [Owning module, declaration or section: bisect](bisect-bisect-left-to-bisect-insort.md)
