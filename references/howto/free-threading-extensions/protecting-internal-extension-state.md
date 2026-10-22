# Protecting Internal Extension State

### Protecting Internal Extension State

Whatever internal state the GIL used to shield inside your extension may now need its own locking from you. The right tactic varies from one extension to the next, yet a few recurring approaches stand out:

- **Caches**: shared state frequently originates in a global cache. Either guard that cache behind a lock, or, when it isn't essential to performance, simply turn it off under the free-threaded build.

- **Global State**: any global state might call for a lock around it, or for relocation into thread-local storage. Both C11 and C++11 supply `thread_local` or `_Thread_local` to give you [thread-local storage](https://en.cppreference.com/w/c/language/storage_duration).

[Subject index](INDEX.md) · [Previous source context](thread-state-and-gil-apis.md) · [Following source context](critical-sections.md)
