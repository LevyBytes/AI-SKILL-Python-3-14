# Formal provability

### Formal provability

One theoretical upside is that constructing a mathematical proof of a functional program's correctness becomes more straightforward.

Researchers have spent considerable time pursuing methods to prove programs correct via mathematics. That differs from running a program across many inputs and inferring that its results are usually right, or from inspecting a program's source and judging that the code seems fine; rather, the aim is a strict proof that a program yields the correct answer across every possible input.

The method for proving programs correct involves writing out **invariants**, which are properties of the input data and of the program's variables that hold true at all times. For every line of code, you then demonstrate that whenever invariants X and Y hold **before** that line runs, the somewhat altered invariants X' and Y' hold **after** the line runs. You repeat this until you arrive at the program's end, where the invariants ought to line up with the intended conditions on the program's output.

Functional programming's reluctance toward assignments came about because assignments are tough to deal with under this method; an assignment can invalidate invariants that held before it without yielding any fresh invariants that could carry forward.

Regrettably, proving programs correct is mostly unworkable and bears little relevance to Python software. Even simple programs demand proofs spanning several pages; the correctness proof for a somewhat involved program would be massive, and hardly any (or none) of the programs you rely on every day (the Python interpreter, your XML parser, your web browser) could ever be proven correct. And even after writing down or generating a proof, you'd still face the matter of checking the proof itself; perhaps it contains a mistake, leading you to mistakenly think you've established the program's correctness.

[Subject index](INDEX.md) · [Previous source context](introduction.md) · [Following source context](modularity.md)
