# How Critical Sections Work

### How Critical Sections Work

In contrast to ordinary locks, a critical section will not promise you exclusive access for its full span. Should a thread end up blocking while it is inside a critical section — by reaching for another lock or doing I/O, say — that critical section pauses, every lock it held is let go, and the whole thing picks back up once the blocking call finishes.

That pattern echoes what the GIL does when a thread makes a blocking call, but several distinctions matter:

- They work one object at a time instead of across the board

- Inside each thread they obey a stack discipline, which the paired, same-scope “begin” and “end” macros impose

- Around anything that might block, they drop their locks and later pick them up again on their own

[Subject index](INDEX.md) · [Previous source context](using-critical-sections.md) · [Following source context](deadlock-avoidance.md)
