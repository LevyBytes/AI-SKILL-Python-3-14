# Blocks, decorators, class and function definitions

```peg
# COMPOUND STATEMENTS
# ===================

# Common elements
# ---------------

block:
    | NEWLINE INDENT statements DEDENT
    | simple_stmts

decorators: ('@' named_expression NEWLINE )+

# Class definitions
# -----------------

class_def:
    | decorators class_def_raw
    | class_def_raw

class_def_raw:
    | 'class' NAME [type_params] ['(' [arguments] ')' ] ':' block

# Function definitions
# --------------------

function_def:
    | decorators function_def_raw
    | function_def_raw

function_def_raw:
    | 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':' [func_type_comment] block
    | 'async' 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':' [func_type_comment] block

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [General statement dispatch and assignment precedence](general-statement-dispatch-and-assignment-precedence.md) · [Function parameters, annotations and defaults](function-parameters-annotations-and-defaults.md) · [Type aliases and type parameter declarations](type-aliases-and-type-parameter-declarations.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Function call arguments and unpacking](function-call-arguments-and-unpacking.md) · [Deletion targets, type expressions and type comments](deletion-targets-type-expressions-and-type-comments.md) · [Previous source section](import-statements-and-dotted-names.md) · [Following source section](function-parameters-annotations-and-defaults.md)
