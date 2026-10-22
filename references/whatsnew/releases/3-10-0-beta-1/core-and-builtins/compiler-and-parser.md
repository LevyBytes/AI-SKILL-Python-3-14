# Python 3.10.0 beta 1 / core and builtins / compiler and parser

[bpo-43683](https://bugs.python.org/issue?@action=redirect&bpo=43683): Introduce the GEN_START opcode. It tags the beginning of a generator ? async ones and coroutines included ? and manages passing values into a freshly built generator or coroutine.

[bpo-43892](https://bugs.python.org/issue?@action=redirect&bpo=43892): Instead of borrowing expression AST nodes, match patterns are now built from purpose-built AST nodes (`MatchValue`, `MatchSingleton`, `MatchSequence`, `MatchStar`, `MatchMapping`, `MatchClass`). The `MatchAs` and `MatchOr` constructs are now classified among the pattern nodes in place of being expression nodes. Nick Coghlan wrote the patch.

[bpo-41323](https://bugs.python.org/issue?@action=redirect&bpo=41323): While folding constant tuples, the bytecode optimizer will now reuse a tuple already sitting in the constant table.

[bpo-43823](https://bugs.python.org/issue?@action=redirect&bpo=43823): Better syntax error reporting for malformed dictionary literals. Pablo Galindo wrote the patch.

[bpo-43822](https://bugs.python.org/issue?@action=redirect&bpo=43822): Better parser syntax errors when commas go missing between expressions. Pablo Galindo wrote the patch.

[bpo-43892](https://bugs.python.org/issue?@action=redirect&bpo=43892): Reinstate correct validation of complex literal value patterns while parsing `match` blocks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
