# Match statements and pattern dispatch

```peg
# Match statement
# ---------------

match_stmt:
    | "match" subject_expr ':' NEWLINE INDENT case_block+ DEDENT

subject_expr:
    | star_named_expression ',' star_named_expressions?
    | named_expression

case_block:
    | "case" patterns guard? ':' block

guard: 'if' named_expression

patterns:
    | open_sequence_pattern
    | pattern

pattern:
    | as_pattern
    | or_pattern

as_pattern:
    | or_pattern 'as' pattern_capture_target

or_pattern:
    | '|'.closed_pattern+

closed_pattern:
    | literal_pattern
    | capture_pattern
    | wildcard_pattern
    | value_pattern
    | group_pattern
    | sequence_pattern
    | mapping_pattern
    | class_pattern

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Blocks, decorators, class and function definitions](blocks-decorators-class-and-function-definitions.md) · [Literal patterns and signed or complex numbers](literal-patterns-and-signed-or-complex-numbers.md) · [Capture, wildcard, value, group and sequence patterns](capture-wildcard-value-group-and-sequence-patterns.md) · [Mapping and class patterns](mapping-and-class-patterns.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Previous source section](if-while-for-with-try-and-exception-clauses.md) · [Following source section](literal-patterns-and-signed-or-complex-numbers.md)
