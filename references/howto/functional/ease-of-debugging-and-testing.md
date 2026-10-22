# Ease of debugging and testing

### Ease of debugging and testing

A functional-style program is simpler to test and debug.

Debugging gets easier since functions tend to be small and precisely defined. Whenever a program misbehaves, each function serves as an interface point where you can confirm the data are right. By examining the intermediate inputs and outputs you can swiftly pinpoint which function is to blame for a bug.

Testing gets easier because every function is a candidate for a unit test. Functions aren't tied to system state that would have to be reproduced ahead of a test; you merely need to fabricate the appropriate input and then verify the output meets expectations.

[Subject index](INDEX.md) · [Previous source context](modularity.md) · [Following source context](composability.md)
