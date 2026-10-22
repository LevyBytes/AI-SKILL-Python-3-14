# 5.1.1. Using Lists as Stacks

### 5.1.1. Using Lists as Stacks

Thanks to the list methods, treating a list as a stack — where whatever was added last is the first thing taken back out ("last-in, first-out") — is straightforward. Push an item onto the top of the stack with [`append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append). Pull an item off the top of the stack with [`pop()`](https://docs.python.org/3.14/library/stdtypes.html#list.pop) and supply no explicit index. As an illustration:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

```

[Subject index](INDEX.md) · [Previous source section](more-on-lists.md) · [Following source section](using-lists-as-queues.md)
