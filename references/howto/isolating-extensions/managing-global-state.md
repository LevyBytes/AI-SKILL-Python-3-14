# Managing Global State

### Making Modules Safe with Multiple Interpreters

### Managing Global State

At times the state bound to a Python module belongs not to that module alone, but to the whole process (or to something else that is ?more global? than a module). As examples:

- The `readline` module governs *the* terminal.

- A module running on a circuit board aims to drive *the* on-board LED.

For situations like these, the Python module ought to expose *access* to the global state instead of *owning* it. Where you can, design the module so that several copies can each reach the state independently (together with other libraries, be they for Python or another language). Where that cannot be done, look into explicit locking.

When process-global state is unavoidable, the easiest route to sidestep trouble with multiple interpreters is to flatly forbid a module from loading more than once per process — refer to Opt-Out: Limiting to One Module Object per Process.

[Subject index](INDEX.md) · [Previous source context](surprising-edge-cases.md) · [Following source context](managing-per-module-state.md)
