# Primary, await, subscript, atom and grouping productions

```peg
# Primary elements
# ----------------

# Primary elements are things like "obj.something.something", "obj[something]", "obj(something)", "obj" ...

await_primary:
    | 'await' primary
    | primary

primary:
    | primary '.' NAME
    | primary genexp
    | primary '(' [arguments] ')'
    | primary '[' slices ']'
    | atom

slices:
    | slice !','
    | ','.(slice | starred_expression)+ [',']

slice:
    | [expression] ':' [expression] [':' [expression] ]
    | named_expression

atom:
    | NAME
    | 'True'
    | 'False'
    | 'None'
    | strings
    | NUMBER
    | (tuple | group | genexp)
    | (list | listcomp)
    | (dict | set | dictcomp | setcomp)
    | '...'

group:
    | '(' (yield_expr | named_expression) ')'

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Formatted and template strings, lists, tuples and sets](formatted-and-template-strings-lists-tuples-and-sets.md) · [Dictionaries, comprehensions and generator expressions](dictionaries-comprehensions-and-generator-expressions.md) · [Function call arguments and unpacking](function-call-arguments-and-unpacking.md) · [Previous source section](comparison-bitwise-and-arithmetic-operator-precedence.md) · [Following source section](lambda-functions-and-lambda-parameter-forms.md)
