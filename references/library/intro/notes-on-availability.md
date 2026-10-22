# Notes on availability

### Notes on availability

- When you see an “Availability: Unix” note, it signals that the function turns up routinely across Unix systems. No assertion is being made about whether it exists on any one particular operating system.

- Unless flagged on their own, every function carrying the “Availability: Unix” label works on macOS, iOS and Android, since each of those is layered over a Unix foundation.

- Should an availability note state both a minimum Kernel version and a minimum libc version, the two requirements apply jointly. Take a feature carrying the note *Availability: Linux >= 3.17 with glibc >= 2.27*: it calls for Linux 3.17 or later together with glibc 2.27 or later.

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](webassembly-platforms.md)
