# Mapping and class patterns

```peg
mapping_pattern:
    | '{' '}'
    | '{' double_star_pattern ','? '}'
    | '{' items_pattern ',' double_star_pattern ','? '}'
    | '{' items_pattern ','? '}'

items_pattern:
    | ','.key_value_pattern+

key_value_pattern:
    | (literal_expr | attr) ':' pattern

double_star_pattern:
    | '**' pattern_capture_target

class_pattern:
    | name_or_attr '(' ')'
    | name_or_attr '(' positional_patterns ','? ')'
    | name_or_attr '(' keyword_patterns ','? ')'
    | name_or_attr '(' positional_patterns ',' keyword_patterns ','? ')'

positional_patterns:
    | ','.pattern+

keyword_patterns:
    | ','.keyword_pattern+

keyword_pattern:
    | NAME '=' pattern

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Match statements and pattern dispatch](match-statements-and-pattern-dispatch.md) · [Literal patterns and signed or complex numbers](literal-patterns-and-signed-or-complex-numbers.md) · [Capture, wildcard, value, group and sequence patterns](capture-wildcard-value-group-and-sequence-patterns.md) · [Previous source section](capture-wildcard-value-group-and-sequence-patterns.md) · [Following source section](type-aliases-and-type-parameter-declarations.md)
