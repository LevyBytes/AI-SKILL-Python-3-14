# Introduction

### Introduction

Regular expressions (known as REs, or regexes, or regex patterns) amount to a small, narrowly focused programming language that ships inside Python and is reachable via the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module. With this miniature language you describe the rules governing the set of strings you intend to match; that collection could hold English sentences, e-mail addresses, TeX commands, or whatever you choose. From there you can pose queries like whether a given string fits the pattern, or whether the pattern turns up somewhere within a string. REs also let you alter a string or break it into pieces in assorted ways.

A regular expression pattern gets compiled down to a sequence of bytecodes that a matching engine, implemented in C, then runs. In demanding scenarios you might have to think carefully about how the engine processes a particular RE, then phrase that RE so its bytecode runs more quickly. Tuning for speed falls outside the scope here, since doing it well presumes a solid grasp of how the matching engine works internally.

Because the regular expression language stays fairly compact and limited, it cannot cover every conceivable string-processing job. Some jobs *are* achievable with regular expressions, yet the resulting expression grows wildly intricate. When that happens, writing plain Python code for the job may serve you better; such code runs more slowly than a baroque regular expression, but it tends to be easier to follow.

[Subject index](INDEX.md) · [Previous source context](regular-expression-howto.md) · [Following source context](simple-patterns.md)
