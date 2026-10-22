# Security and threat model

### Security and threat model

Underneath, the remote debugging protocol leans on the very same operating-system primitives that native debuggers like GDB and LLDB depend on. Hooking into a process demands the **same privileges** those debuggers do — `ptrace` / Yama LSM under Linux, `task_for_pid` on macOS, and `SeDebugPrivilege` on Windows, to name a few. No fresh privilege-escalation avenue is opened up by Python here; an attacker who already holds the rights required to attach to a process could just as well turn to GDB to inspect memory or plant code.

These guidelines spell out which conditions do, and do not, count as a security vulnerability for this feature:

Attaching requires OS-level privileges

Across all supported platforms, reaching into another process's memory is something the OS guards behind privilege checks (`CAP_SYS_PTRACE`, root, or administrator rights). Should a report only surface its problem once those privileges are in hand, that is **not** a CPython vulnerability, because the operating system's security boundary had already been breached beforehand.

Crashes or memory errors when reading a compromised process are not vulnerabilities

Any tool that pulls internal interpreter state out of a target process has to assume that memory is well-formed. Where the target has been tampered with or is in an attacker's hands, the debugger or profiler might crash, spit out nonsense, or act erratically. That is precisely the hazard every `ptrace`-based debugger already lives with. Defects of this sort — buffer overflows, segmentation faults, or undefined behaviour set off by reading corrupted state — are **not** classed as security problems, although patches that harden robustness are still welcome.

Vulnerabilities in the target process are not in scope

When the Python process under debug has already fallen to an attacker, that attacker is by then directing execution inside it. Showing additional damage starting from that position is not, in itself, a flaw in the remote debugging protocol.

[Subject index](INDEX.md) · [Previous source context](summary.md) · [Following source context](when-to-use-python-disable-remote-debug.md)
