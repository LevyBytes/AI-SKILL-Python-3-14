# Why is join() a string method instead of a list or tuple method?

### Why is join() a string method instead of a list or tuple method?

From Python 1.6 onward, strings grew far closer to the other standard types when methods arrived that deliver the same capability long offered through the functions in the string module. The bulk of these new methods met with broad acceptance, but the one that seems to leave certain programmers ill at ease is:

```python
", ".join(['1', '2', '4', '8', '16'])

```

which yields the result:

```python
"1, 2, 4, 8, 16"

```

Two arguments are commonly raised against this usage.

The first goes roughly: "Calling a method on a string literal (string constant) looks really ugly", to which the response is that maybe it does, yet a literal string is no more than a fixed value. If such methods may apply to names bound to strings, there's no logical basis for denying them to literals.

The second objection usually takes the shape: "What I'm really doing is asking a sequence to stitch its members together using a string constant". Regrettably, you aren't. For whatever reason, people seem to struggle far less with [`split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split) being a string method, since in that instance it's plain to see that

```python
"1, 2, 4, 8, 16".split(", ")

```

directs a string literal to hand back the substrings separated by the supplied separator (or, by default, arbitrary stretches of white space).

[`join()`](https://docs.python.org/3.14/library/stdtypes.html#str.join) is a string method because employing it means you are directing the separator string to iterate across a sequence of strings and place itself between neighboring elements. The method accepts any argument that follows the rules for sequence objects, including any new classes of your own design. Comparable methods are available for bytes and bytearray objects.

[Subject index](INDEX.md)
