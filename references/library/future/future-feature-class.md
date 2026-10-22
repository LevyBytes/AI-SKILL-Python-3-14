# __future__: `__future__._Feature`

### Module Contents

A feature description is never removed from `__future__` once added. From its debut in Python 2.1 onward, the features below have entered the language through this mechanism:

| feature | optional in | mandatory in | effect |
| --- | --- | --- | --- |
| __future__.nested_scopes | 2.1.0b1 | 2.2 | **PEP 227**: *Statically Nested Scopes* |
| __future__.generators | 2.2.0a1 | 2.3 | **PEP 255**: *Simple Generators* |
| __future__.division | 2.2.0a2 | 3.0 | **PEP 238**: *Changing the Division Operator* |
| __future__.absolute_import | 2.5.0a1 | 3.0 | **PEP 328**: *Imports: Multi-Line and Absolute/Relative* |
| __future__.with_statement | 2.5.0a1 | 2.6 | **PEP 343**: *The “with” Statement* |
| __future__.print_function | 2.6.0a2 | 3.0 | **PEP 3105**: *Make print a function* |
| __future__.unicode_literals | 2.6.0a2 | 3.0 | **PEP 3112**: *Bytes literals in Python 3000* |
| __future__.generator_stop | 3.5.0b1 | 3.7 | **PEP 479**: *StopIteration handling inside generators* |
| __future__.annotations | 3.7.0b1 | Never [1] | **PEP 563**: *Postponed evaluation of annotations*; and **PEP 649**, which covers deferred annotation evaluation done through descriptors |

 `*class *__future__._Feature`

Within `__future__.py`, every statement takes this shape:

```python
FeatureName = _Feature(OptionalRelease, MandatoryRelease,
                       CompilerFlag)

```

in which, as a rule, *OptionalRelease* comes before *MandatoryRelease*, and each is a 5-tuple laid out just like [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info):

```python
(PY_MAJOR_VERSION, # the 2 in 2.1.0a3; an int
 PY_MINOR_VERSION, # the 1; an int
 PY_MICRO_VERSION, # the 0; an int
 PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" or "final"; string
 PY_RELEASE_SERIAL # the 3; an int
)

```

[Subject index](INDEX.md) · [Previous](future-future-statement-definitions.md) · [Continue](feature-getoptionalrelease-to-feature-compiler-flag.md) · [Owning module, declaration or section: __future__](future-future-statement-definitions.md)
