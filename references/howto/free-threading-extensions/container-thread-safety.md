# Container Thread Safety

### Container Thread Safety

Within the free-threaded build, container types — [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject), [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject), and [`PySetObject`](https://docs.python.org/3.14/c-api/set.html#c.PySetObject) among them — handle their own locking internally. To illustrate, [`PyList_Append()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Append) takes the list's lock first and only then adds the new item.

[Subject index](INDEX.md) · [Previous source context](general-api-guidelines.md) · [Following source context](pydict-next.md)
