# Why are Python strings immutable?

### Why are Python strings immutable?

The benefits are several.

The first is performance: when we know a string can't change, we can set aside room for it the moment it's created, and the amount of storage it needs stays fixed and constant. This also forms part of the rationale for separating tuples from lists.

A further benefit is that Python regards strings as just as "elemental" as numbers are. No quantity of activity will turn the value 8 into anything different, and likewise in Python no quantity of activity will turn the string "eight" into anything different.

[Subject index](INDEX.md)
