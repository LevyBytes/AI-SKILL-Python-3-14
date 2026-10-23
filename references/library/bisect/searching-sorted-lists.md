# bisect - Searching Sorted Lists

### Searching Sorted Lists

Handy as the bisect functions above are for locating insertion points, they can prove fiddly or clumsy when applied to everyday searching jobs. The five functions below illustrate how to recast them into the usual lookups over sorted lists:

```python
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

```

[Subject index](INDEX.md) · [Previous](performance-notes.md) · [Continue](examples.md) · [Owning module, declaration or section: bisect](bisect-bisect-left-to-bisect-insort.md)
