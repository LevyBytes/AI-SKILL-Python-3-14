# pdb — Debugger commands — Contract: Disable the breakpoints supplied as a space-separated list of breakpoint numbers.

Disable the breakpoints supplied as a space-separated list of breakpoint numbers. A disabled breakpoint can no longer halt the program, yet unlike a cleared one it stays in the breakpoint list and can be re-enabled later.

 enable bpnumber [bpnumber ...]

Enable the breakpoints specified.

 ignore bpnumber [count]

Set the ignore count for the supplied breakpoint number. When *count* is left out, the ignore count becomes 0. A breakpoint turns active once its ignore count reaches zero. While non-zero, the *count* drops by one each time the breakpoint is hit, provided the breakpoint is not disabled and any condition tied to it evaluates to true.

 condition bpnumber [condition]

Attach a new *condition* to the breakpoint, an expression that has to evaluate to true for the breakpoint to take effect. When *condition* is missing, any existing condition is dropped; that is, the breakpoint becomes unconditional.

 commands [bpnumber]

Provide a list of commands for breakpoint number *bpnumber*. Those commands go on the lines that follow. End the list by typing a line that contains only `end`. An example:

```python
(Pdb) commands 1
(com) p some_variable
(com) end
(Pdb)

```

To strip every command from a breakpoint, type `commands` and immediately follow it with `end`; in other words, supply no commands.

When no *bpnumber* argument is given, `commands` applies to the most recently set breakpoint.

Breakpoint commands can be used to get your program running again. Just use the `continue` command, or `step`, or any other command that resumes execution.

Giving any command that resumes execution (at present `continue`, `step`, `next`, `return`, `until`, `jump`, `quit` and their abbreviations) ends the command list (as though that command were immediately followed by end). The reason is that whenever you resume execution (even with a plain next or step), you might hit another breakpoint—which might carry its own command list, raising the question of which list should run.

When the command list holds the `silent` command, or a command that resumes execution, the breakpoint message that carries the frame information is suppressed.

Changed in version 3.14: When the command list contains a command that resumes execution, the frame information is no longer shown.

[Subject index](INDEX.md) · [Previous](debugger-commands-section-introduction-and-initial-examples.md) · [Continue](s-to-c.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Debugger commands](debugger-commands-section-introduction-and-initial-examples.md)
