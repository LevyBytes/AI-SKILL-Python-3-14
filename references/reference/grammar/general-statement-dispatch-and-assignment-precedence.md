# General statement dispatch and assignment precedence

[Following source section](assignment-and-simple-statement-productions.md)

```peg
# GENERAL STATEMENTS
# ==================

statements: statement+

statement:
    | compound_stmt
    | simple_stmts

single_compound_stmt:
    | compound_stmt

statement_newline:
    | single_compound_stmt NEWLINE
    | simple_stmts
    | NEWLINE
    | ENDMARKER

simple_stmts:
    | simple_stmt !';' NEWLINE  # Not needed, there for speedup
    | ';'.simple_stmt+ [';'] NEWLINE

# NOTE: assignment MUST precede expression, else parsing a simple assignment
# will throw a SyntaxError.
simple_stmt:
    | assignment
    | type_alias
    | star_expressions
    | return_stmt
    | import_stmt
    | raise_stmt
    | pass_stmt
    | del_stmt
    | yield_stmt
    | assert_stmt
    | break_stmt
    | continue_stmt
    | global_stmt
    | nonlocal_stmt

compound_stmt:
    | function_def
    | if_stmt
    | class_def
    | with_stmt
    | for_stmt
    | try_stmt
    | while_stmt
    | match_stmt

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Assignment and simple statement productions](assignment-and-simple-statement-productions.md) · [Blocks, decorators, class and function definitions](blocks-decorators-class-and-function-definitions.md) · [If, while, for, with, try and exception clauses](if-while-for-with-try-and-exception-clauses.md) · [Match statements and pattern dispatch](match-statements-and-pattern-dispatch.md) · [Type aliases and type parameter declarations](type-aliases-and-type-parameter-declarations.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Previous source section](peg-notation-parser-passes-cuts-and-starting-rules.md)
