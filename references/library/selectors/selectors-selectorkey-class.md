# selectors: `selectors.SelectorKey`

### Classes

Classes hierarchy:

```python
BaseSelector
+-- SelectSelector
+-- PollSelector
+-- EpollSelector
+-- DevpollSelector
+-- KqueueSelector

```

In what comes next, *events* names a bitwise mask spelling out the I/O events to await on a particular file object. You may form it by combining the module’s constants listed here:

>
| Constant | Meaning |
| --- | --- |
| selectors.EVENT_READ | Available for read |
| selectors.EVENT_WRITE | Available for write |

 *class *selectors.SelectorKey

Built as a [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple), a `SelectorKey` ties a file object together with its backing file descriptor, the chosen event mask, plus any data hung off it. A number of `BaseSelector` methods hand one back.

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](classes.md) · [Owning module, declaration or section: selectors](selectors-high-level-i-o-multiplexing.md)
