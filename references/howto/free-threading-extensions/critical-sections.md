# Critical Sections

### Critical Sections

Under the free-threaded build, CPython offers a facility termed “critical sections” for safeguarding data that the GIL would otherwise have covered. Even though extension writers rarely touch the underlying critical-section machinery themselves, grasping how it behaves matters a great deal once you start calling particular C API functions or holding shared state in this build.

[Subject index](INDEX.md) · [Previous source context](protecting-internal-extension-state.md) · [Following source context](what-are-critical-sections.md)
