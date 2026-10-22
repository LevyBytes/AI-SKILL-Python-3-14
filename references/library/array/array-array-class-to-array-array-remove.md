# array: `array.array`, `append()`, `buffer_info()`, `byteswap()`, `count()`, `extend()`, `frombytes()`, `fromfile()`, `fromlist()`, `fromunicode()`, `index()`, `insert()`, `pop()`, `remove()`

*class *array.array(*typecode*[, *initializer*])

A fresh array whose elements are constrained by *typecode* and seeded from the optional *initializer* value; that value has to be a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object, a Unicode string, or an iterable yielding elements of the right type.

When the initializer is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object, it goes to the new array’s `frombytes()` method; when it is a Unicode string, it goes to the `fromunicode()` method; in every other case its iterator is fed to the `extend()` method so the array starts out with those items.

The usual [mutable](https://docs.python.org/3.14/library/stdtypes.html#typesseq-mutable) [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) operations — indexing, slicing, concatenation, and multiplication — all work on array objects. For slice assignment, the value assigned has to be an array object carrying the same type code; anything else triggers [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Array objects also satisfy the buffer interface, so they fit anywhere [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) are accepted.

With respect to the type they hold, arrays are [generic](https://docs.python.org/3.14/library/typing.html#generics).

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `array.__new__` carrying the arguments `typecode`, `initializer`.

 typecode

The character of the typecode that the array was built from.

 itemsize

How many bytes a single array item occupies in the internal layout.

 append(*value*, */*)

Tack a new item holding the given value onto the array’s tail.

 buffer_info()

Hand back a tuple `(address, length)` that reports the present memory address together with the element count of the buffer that stores the array’s contents. You can work out the buffer’s byte size as `array.buffer_info()[1] * array.itemsize`. Now and then this comes in handy with low-level — and by nature unsafe — I/O interfaces that demand memory addresses, certain `ioctl()` operations among them. The figures returned stay accurate for as long as the array lives and nothing alters its length.

Note

If you are reaching array objects from C or C++ code — really the only context in which this information is of any use — the buffer interface that array objects expose is the better choice. The present method survives purely for backward compatibility, so steer clear of it in fresh code. Documentation for the buffer interface appears under [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

 byteswap()

“Byteswap” every item the array holds. Only values that occupy 1, 2, 4, or 8 bytes qualify; with any other value size, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised. It comes in handy when you read data from a file that was written on a machine using a different byte order.

 count(*value*, */*)

Give back how many times *value* shows up in the array.

 extend(*iterable*, */*)

Tack the items from *iterable* onto the array’s tail. Should *iterable* itself be an array, it has to carry *exactly* the matching type code, or a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised. When *iterable* is not an array, it merely needs to be iterable and to yield elements whose type is suitable for appending to the array.

 frombytes(*buffer*, */*)

Tacks on items drawn from the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), reading its content as an array of machine values — just as though it had been pulled from a file via the `fromfile()` method.

Added in version 3.2: For the sake of clarity, `fromstring()` was renamed `frombytes()`.

 fromfile(*f*, *n*, */*)

Pull *n* items (as machine values) out of the [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *f* and tack them onto the array’s tail. Where fewer than *n* items can be had, an [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError) is raised, yet whatever items were available still land in the array.

 fromlist(*list*, */*)

Tack the list’s items on. It amounts to `for x in list: a.append(x)`, with the one distinction that a type error leaves the array untouched.

 fromunicode(*ustr*, */*)

Grows this array using the contents of the supplied Unicode string. Its type code has to be `'u'` or `'w'`, or else a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results. To tack Unicode data onto an array of any other type, call `array.frombytes(unicodestring.encode(enc))`.

 index(*value*[, *start*[, *stop*]])

Give back the smallest *i* that marks where *value* first appears in the array. Supplying the optional *start* and *stop* arguments lets you confine the hunt for *value* to a slice of the array. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when *value* turns up nowhere.

Changed in version 3.10: The optional *start* and *stop* parameters were introduced.

 insert(*index*, *value*, */*)

Place a new item *value* into the array just ahead of position *index*. A negative figure is read as counting back from the array’s end.

 pop(*index=-1*, */*)

Takes the item at index *i* out of the array and hands it back. Because the optional argument defaults to `-1`, the final item is the one removed and returned unless you say otherwise.

 remove(*value*, */*)

Strip out the first instance of *value* found in the array.

[Subject index](INDEX.md) · [Previous](array-typecodes.md) · [Continue](array-array-clear-to-array-array-tounicode.md) · [Owning module, declaration or section: array](array-typecodes.md)
