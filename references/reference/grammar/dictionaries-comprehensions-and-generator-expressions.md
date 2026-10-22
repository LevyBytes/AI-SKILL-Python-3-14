# Dictionaries, comprehensions and generator expressions

```peg
# Dicts
# -----

dict:
    | '{' [double_starred_kvpairs] '}'

double_starred_kvpairs: ','.double_starred_kvpair+ [',']

double_starred_kvpair:
    | '**' bitwise_or
    | kvpair

kvpair: expression ':' expression

# Comprehensions & Generators
# ---------------------------

for_if_clauses:
    | for_if_clause+

for_if_clause:
    | 'async' 'for' star_targets 'in' ~ disjunction ('if' disjunction )*
    | 'for' star_targets 'in' ~ disjunction ('if' disjunction )*

listcomp:
    | '[' named_expression for_if_clauses ']'

setcomp:
    | '{' named_expression for_if_clauses '}'

genexp:
    | '(' ( assignment_expression | expression !':=') for_if_clauses ')'

dictcomp:
    | '{' kvpair for_if_clauses '}'

```

[Subject index](INDEX.md) · [Grammar scope and omitted parser actions](full-grammar-scope-notation-and-omitted-parser-actions.md) · [PEG notation and parser passes](peg-notation-parser-passes-cuts-and-starting-rules.md) · [Expressions, yields, named expressions and boolean operators](expressions-yields-named-expressions-and-boolean-operators.md) · [Comparison, bitwise and arithmetic operator precedence](comparison-bitwise-and-arithmetic-operator-precedence.md) · [Assignment targets and target lookahead](assignment-targets-and-target-lookahead.md) · [Previous source section](formatted-and-template-strings-lists-tuples-and-sets.md) · [Following source section](function-call-arguments-and-unpacking.md)
