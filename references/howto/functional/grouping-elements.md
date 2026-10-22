# Grouping elements

### Grouping elements

The final function I'll cover, [`itertools.groupby(iter, key_func=None)`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby), is the trickiest one. `key_func(elem)` is a function capable of deriving a key value from each element the iterable yields. When you leave out a key function, the key defaults to the element on its own.

[`groupby()`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby) gathers every run of adjacent elements from the underlying iterable sharing one key value, then yields a stream of 2-tuples, each holding a key value plus an iterator over the elements carrying that key.

```python
city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
             ...
            ]

def get_state(city_state):
    return city_state[1]

itertools.groupby(city_list, get_state) =>
  ('AL', iterator-1),
  ('AK', iterator-2),
  ('AZ', iterator-3), ...

where
iterator-1 =>
  ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
iterator-2 =>
  ('Anchorage', 'AK'), ('Nome', 'AK')
iterator-3 =>
  ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')

```

[`groupby()`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby) presumes that the underlying iterable already arrives sorted on the key. Keep in mind that the iterators handed back also draw from that same underlying iterable, so you must finish consuming iterator-1's results before you ask for iterator-2 and the key that goes with it.

[Subject index](INDEX.md) · [Previous source context](combinatoric-functions.md) · [Following source context](the-functools-module.md)
