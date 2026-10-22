# Important Considerations

### Important Considerations

- Because a critical section can briefly surrender its locks, another thread is then free to alter the very data you meant to protect. Stay wary of any assumption about that data's condition following a call that could block.

- Since locks can be handed back for a while (suspended), stepping into a critical section is no promise of sole access to the guarded resource for the section's whole length. The moment code inside it calls some other blocking function — taking a second lock, doing blocking I/O, and so on — the thread releases every lock it was holding by way of critical sections. The GIL behaves much the same way, giving itself up during blocking calls.

- At any instant, the sole locks you can count on still being held belong to the section entered most recently — the top-most one. The locks tied to outer, enclosing critical sections may well sit suspended.

- These APIs cap you at two objects locked together at once. Should your design demand more than that, you'll have to reshape the code.

- Locking one and the same object twice won't deadlock a critical section, yet for that scenario they run slower than reentrant locks made for the job.

- With [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2), which object comes first has no effect on correctness — the implementation takes care of avoiding deadlock — but settling on one consistent locking order remains sound practice.

- Bear in mind that the critical-section macros exist chiefly to guard access to *Python objects* that could be caught up in internal CPython work prone to the deadlock cases laid out above. To shield extension state that is wholly internal, a plain mutex or another synchronization primitive may serve you better.

[Subject index](INDEX.md) · [Previous source context](deadlock-avoidance.md) · [Following source context](building-extensions-for-the-free-threaded-build.md)
