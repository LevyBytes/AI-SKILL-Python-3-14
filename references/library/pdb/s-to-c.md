# pdb / Debugger commands: Debugger stepping, continuation, jumps and source listing

s(tep)

Run the current line and stop at the earliest opportunity (either inside a function that gets called or on the next line of the current function).

 n(ext)

Keep running until the next line of the current function is reached or it returns. (`next` differs from `step` in that `step` halts inside a called function, whereas `next` runs called functions at (nearly) full speed and stops only at the next line of the current function.)

 unt(il) [lineno]

With no argument, keep running until reaching a line whose number is greater than the current one.

With *lineno*, keep running until reaching a line whose number is greater than or equal to *lineno*. In either case, also stop when the current frame returns.

Changed in version 3.2: Allow giving an explicit line number.

 r(eturn)

Continue execution until the current function returns.

 c(ont(inue))

Continue execution, only stop when a breakpoint is encountered.

 j(ump) lineno

Set the next line to be executed. Available only in the bottom-most frame. This lets you jump back to rerun code, or jump ahead to skip code you would rather not run.

Keep in mind that not every jump is permitted – for example, you cannot jump into the middle of a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop or out of a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause.

 l(ist) [first[, last]]

List source code for the current file. Given no arguments, it shows 11 lines centered on the current line or resumes the prior listing. Given `.` as the argument, it shows 11 lines centered on the current line. Given one argument, it shows 11 lines centered on that line. Given two arguments, it shows the supplied range; should the second argument fall below the first, that value is read as a count instead.

In the current frame, the current line is shown by `->`. When an exception is being debugged, the line where it was first raised or propagated is shown by `>>`, provided that differs from the current line.

Changed in version 3.2: Added the `>>` marker.

 ll | longlist

Show the complete source code of the current function or frame. Noteworthy lines carry the same markings as in `list`.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](disabling-debugger-breakpoints.md) · [Continue](a.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Debugger commands](debugger-commands-section-introduction-and-initial-examples.md)
