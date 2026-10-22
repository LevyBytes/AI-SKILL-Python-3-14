# Generator expressions and list comprehensions syntax and filtering

### Generator expressions and list comprehensions

Two frequent operations applied to an iterator's output are 1) carrying out some operation on every element, 2) picking a subset of elements satisfying some condition. As an example, given a list of strings, you might wish to strip trailing whitespace from each line or pull out all the strings holding a particular substring.

List comprehensions and generator expressions (in short form: "listcomps" and "genexps") offer a compact notation for these operations, taken from the functional programming language Haskell ([https://www.haskell.org/](https://www.haskell.org/)). You can remove all the whitespace from a stream of strings using the code below:

```python
>>> line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

>>> # Generator expression -- returns iterator
>>> stripped_iter = (line.strip() for line in line_list)

>>> # List comprehension -- returns list
>>> stripped_list = [line.strip() for line in line_list]

```

You can keep only particular elements by attaching an `"if"` condition:

```python
>>> stripped_list = [line.strip() for line in line_list
...                  if line != ""]

```

When using a list comprehension, what you receive back is a Python list; `stripped_list` is a list holding the resulting lines, not an iterator. Generator expressions hand back an iterator that computes values on demand, without having to materialize all of the values up front. That means list comprehensions don't help if you're dealing with iterators that yield an unending stream or an enormous amount of data. In such cases, generator expressions are the better choice.

Parentheses ("()") enclose generator expressions, whereas square brackets ("[]") enclose list comprehensions. Generator expressions take this form:

```python
( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3
             ...
             if condition3
             for exprN in sequenceN
             if conditionN )

```

Once more, for a list comprehension only the outer brackets change (square brackets in place of parentheses).

The elements of the produced output will be the consecutive values of `expression`. Every `if` clause is optional; when one is present, `expression` is evaluated and added to the result only if `condition` holds true.

Generator expressions must always sit inside parentheses, although the parentheses denoting a function call qualify too. If you wish to build an iterator that gets passed straight to a function you can write:

```python
obj_total = sum(obj.count for obj in list_all_objects())

```

[Subject index](INDEX.md) · [Nested iteration products and tuple-expression syntax](nested-iteration-products-and-tuple-expression-syntax.md) · [Previous source context](data-types-that-support-iterators.md) · [Following source context](nested-iteration-products-and-tuple-expression-syntax.md)
