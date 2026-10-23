# bdb`bdb` - Debugger framework

bdb.checkfuncname(*b*, *frame*)

Return `True` when we ought to break here, contingent on the manner in which the `Breakpoint` *b* was set.

When it was set by line number, it checks whether `b.line` matches the one in *frame*. When the breakpoint was set by `function name`, we must confirm we are in the right *frame* (the right function) and that we are on its first executable line.

 bdb.effective(*file*, *line*, *frame*)

Return `(active breakpoint, delete temporary flag)` or `(None, None)` as the breakpoint to act upon.

Within `bplist`, the *active breakpoint* is the earliest entry for the (`file`, `line`) pair (which has to exist) where the entry is `enabled`, where `checkfuncname()` holds true, and where it carries neither a false `condition` nor a positive `ignore` count. The *flag*, signaling that a temporary breakpoint should be deleted, is `False` only where the `cond` cannot be evaluated (whereupon the `ignore` count is ignored).

Should no such entry exist, then `(None, None)` is returned.

 bdb.set_trace()

Start debugging with a `Bdb` instance from caller's frame.

[Subject index](INDEX.md) · [Previous](bdb-bdb-format-stack-entry-to-bdb-bdb-runcall.md) · [Continue](../binary/binary-data-services.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md)
