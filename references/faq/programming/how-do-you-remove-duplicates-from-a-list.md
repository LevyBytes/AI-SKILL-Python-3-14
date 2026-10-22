# How do you remove duplicates from a list?

### How do you remove duplicates from a list?

The Python Cookbook holds a lengthy discussion of the many ways to accomplish this:

>

[https://code.activestate.com/recipes/52560/](https://code.activestate.com/recipes/52560/)

Provided that reordering the list is acceptable, sort it and then walk from the list's end, removing duplicates along the way:

```python
if mylist:
    mylist.sort()
    last = mylist[-1]
    for i in range(len(mylist)-2, -1, -1):
        if last == mylist[i]:
            del mylist[i]
        else:
            last = mylist[i]

```

Should every element of the list be usable as a set key (meaning they are all [hashable](https://docs.python.org/3.14/glossary.html#term-hashable)), this is frequently faster:

```python
mylist = list(set(mylist))

```

This turns the list into a set, which strips out duplicates, then turns it back into a list.

[Subject index](INDEX.md)
