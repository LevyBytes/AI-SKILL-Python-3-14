# Deletion targets, type expressions and type comments

```peg
# Targets for del statements
# --------------------------

del_targets: ','.del_target+ [',']

del_target:
    | t_primary '.' NAME !t_lookahead
    | t_primary '[' slices ']' !t_lookahead
    | del_t_atom

del_t_atom:
    | NAME
    | '(' del_target ')'
    | '(' [del_targets] ')'
    | '[' [del_targets] ']'

# TYPING ELEMENTS
# ---------------

# type_expressions allow */** but ignore them
type_expressions:
    | ','.expression+ ',' '*' expression ',' '**' expression
    | ','.expression+ ',' '*' expression
    | ','.expression+ ',' '**' expression
    | '*' expression ',' '**' expression
    | '*' expression
    | '**' expression
    | ','.expression+

func_type_comment:
    | NEWLINE TYPE_COMMENT &(NEWLINE INDENT)   # Must be followed by indented block
    | TYPE_COMMENT

# ========================= END OF THE GRAMMAR ===========================

# ========================= START OF INVALID RULES =======================

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Primary, await, subscript, atom and grouping productions](primary-await-subscript-atom-and-grouping-productions.md) · [Assignment targets and target lookahead](assignment-targets-and-target-lookahead.md) · [Previous source section](assignment-targets-and-target-lookahead.md)
