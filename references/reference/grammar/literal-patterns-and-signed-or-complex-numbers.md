# Literal patterns and signed or complex numbers

```peg
# Literal patterns are used for equality and identity constraints
literal_pattern:
    | signed_number !('+' | '-')
    | complex_number
    | strings
    | 'None'
    | 'True'
    | 'False'

# Literal expressions are used to restrict permitted mapping pattern keys
literal_expr:
    | signed_number !('+' | '-')
    | complex_number
    | strings
    | 'None'
    | 'True'
    | 'False'

complex_number:
    | signed_real_number '+' imaginary_number
    | signed_real_number '-' imaginary_number

signed_number:
    | NUMBER
    | '-' NUMBER

signed_real_number:
    | real_number
    | '-' real_number

real_number:
    | NUMBER

imaginary_number:
    | NUMBER

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Formatted and template strings, lists, tuples and sets](formatted-and-template-strings-lists-tuples-and-sets.md) · [Previous source section](match-statements-and-pattern-dispatch.md) · [Following source section](capture-wildcard-value-group-and-sequence-patterns.md)
