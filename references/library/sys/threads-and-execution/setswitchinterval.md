# sys.setswitchinterval

sys.setswitchinterval(*interval*)

Define the interpreter’s thread switch interval, measured in seconds. This floating-point quantity fixes the ideal length of the “timeslices” granted to Python threads that run concurrently. Be aware that the real value can run higher, particularly when long-running internal functions or methods are involved. Furthermore, the choice of which thread is scheduled once the interval ends belongs to the operating system. The interpreter carries no scheduler of its own.

Added in version 3.2.

[API family](INDEX.md) · [sys context index](../INDEX.md).
