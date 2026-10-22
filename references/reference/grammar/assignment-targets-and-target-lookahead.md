# Assignment targets and target lookahead

```peg
# ASSIGNMENT TARGETS
# ==================

# Generic targets
# ---------------

# NOTE: star_targets may contain *bitwise_or, targets may not.
star_targets:
    | star_target !','
    | star_target (',' star_target )* [',']

star_targets_list_seq: ','.star_target+ [',']

star_targets_tuple_seq:
    | star_target (',' star_target )+ [',']
    | star_target ','

star_target:
    | '*' (!'*' star_target)
    | target_with_star_atom

target_with_star_atom:
    | t_primary '.' NAME !t_lookahead
    | t_primary '[' slices ']' !t_lookahead
    | star_atom

star_atom:
    | NAME
    | '(' target_with_star_atom ')'
    | '(' [star_targets_tuple_seq] ')'
    | '[' [star_targets_list_seq] ']'

single_target:
    | single_subscript_attribute_target
    | NAME
    | '(' single_target ')'

single_subscript_attribute_target:
    | t_primary '.' NAME !t_lookahead
    | t_primary '[' slices ']' !t_lookahead

t_primary:
    | t_primary '.' NAME &t_lookahead
    | t_primary '[' slices ']' &t_lookahead
    | t_primary genexp &t_lookahead
    | t_primary '(' [arguments] ')' &t_lookahead
    | atom &t_lookahead

t_lookahead: '(' | '[' | '.'

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Primary, await, subscript, atom and grouping productions](primary-await-subscript-atom-and-grouping-productions.md) · [Dictionaries, comprehensions and generator expressions](dictionaries-comprehensions-and-generator-expressions.md) · [Function call arguments and unpacking](function-call-arguments-and-unpacking.md) · [Previous source section](function-call-arguments-and-unpacking.md) · [Following source section](deletion-targets-type-expressions-and-type-comments.md)
