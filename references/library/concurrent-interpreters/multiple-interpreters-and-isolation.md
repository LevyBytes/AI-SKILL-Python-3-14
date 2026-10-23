# concurrent.interpreters - Multiple Interpreters and Isolation

### Multiple Interpreters and Isolation

It’s up to a given Python implementation whether it permits several interpreters in one process. CPython does permit it. For all practical purposes each interpreter stands apart from the rest (barring a small, carefully handled set of process-global exceptions to that rule).

What makes that isolation valuable is mostly the firm boundary it draws between a program’s separate logical pieces, in places where you want tight control over how those pieces talk to one another.

Note

Strictly speaking, interpreters sharing a process can never be perfectly walled off from each other, because almost nothing restricts memory access inside a single process. The Python runtime tries its hardest to isolate them, but an extension module can break that with ease. For that reason, steer clear of multiple interpreters in security-sensitive scenarios where they ought not see each other’s data.

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](running-in-an-interpreter.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
