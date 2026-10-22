# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Declarative approach

#### Declarative approach

Some readers may already know pattern matching from the basic case of pairing a subject (data object) against a literal (pattern) via the switch statement seen in C, Java or JavaScript (plus numerous other languages). The switch statement frequently serves to compare an object or expression against case statements that hold literals.

Richer demonstrations of pattern matching turn up in languages like Scala and Elixir. The structural pattern matching style is "declarative" and spells out plainly the conditions (the patterns) that data has to satisfy.

You could indeed reach for an "imperative" run of steps built from nested "if" statements to mimic structural pattern matching, but it reads less clearly than the "declarative" route. The "declarative" route instead lays out the conditions a match must satisfy and reads more easily thanks to its explicit patterns. Even though structural pattern matching can serve in its barest form, comparing a variable against a literal within a case statement, where it really earns its keep for Python is in dealing with the type and shape of the subject.

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-syntax-and-operations.md) · [Next source section](literal-pattern-matching.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
