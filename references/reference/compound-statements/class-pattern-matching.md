# compound statements: Class-pattern syntax and matching rules

#### 8.6.4.10. Class Patterns

A class together with its positional and keyword arguments (where present) is represented by a class pattern. Syntax:

```text

class_pattern:       name_or_attr "(" [pattern_arguments ","?] ")"
pattern_arguments:   positional_patterns ["," keyword_patterns]
                     | keyword_patterns
positional_patterns: ",".pattern+
keyword_patterns:    ",".keyword_pattern+
keyword_pattern:     NAME "=" pattern
```

A keyword must not appear more than once within a class pattern.

Matching a class pattern against a subject value proceeds logically as follows:

1.

When `name_or_attr` is not an instance of the builtin [`type`](https://docs.python.org/3.14/library/functions.html#type) , a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

2.

When the subject value is not an instance of `name_or_attr` (checked with [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance)), the class pattern fails.

3.

When no pattern arguments appear, the pattern passes. Otherwise, what follows depends on whether keyword or positional argument patterns are present.

A handful of built-in types (listed below) accept a single positional subpattern that matches the whole subject; for those types keyword patterns behave as they do for any other type.

When only keyword patterns appear, each is handled in turn like this:

  1.

The keyword is fetched as an attribute on the subject.

    - When this throws an exception that is not [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), the exception propagates outward.

    - When this throws [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), the class pattern has failed.

    - Otherwise the keyword pattern's associated subpattern is matched against that attribute value on the subject. A failure here fails the class pattern; on success the match moves to the following keyword.

  2.

When every keyword pattern passes, the class pattern passes.

Whenever positional patterns appear, they are first turned into keyword patterns by means of the [`__match_args__`](https://docs.python.org/3.14/reference/datamodel.html#object.__match_args__) attribute on the class `name_or_attr`:

  1.

The equivalent of `getattr(cls, "__match_args__", ())` is called.

    - Should this throw an exception, the exception propagates outward.

    - Should the value returned not be a tuple, the conversion fails and a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

    - Should the positional patterns outnumber `len(cls.__match_args__)`, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

    - Otherwise positional pattern `i` becomes a keyword pattern, using `__match_args__[i]` as its keyword. `__match_args__[i]` has to be a string; otherwise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

    - Should keywords be duplicated, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

See also

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](mapping-patterns.md) · [Following source section](class-patterns-2.md)
