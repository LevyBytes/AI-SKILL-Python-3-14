# Differences Between Unix and Windows — Py_NO_LINK_LIB

### 5.2. Differences Between Unix and Windows

When it comes to loading code at run time, Unix and Windows follow entirely distinct models. So before attempting to construct a module meant to load dynamically, make sure you understand how your platform handles it.

On Unix, a shared object (`.so`) file bundles the code the program will call, alongside the names of the functions and data it anticipates locating within that program. Once the file gets bound to the program, every reference inside the file's code to those functions and data is rewritten so it aims at the real spots in memory where the program has placed them. At heart this amounts to a link operation.

On Windows, by contrast, a dynamic-link library (`.dll`) file carries no unresolved references. Reaching any function or piece of data instead routes through a lookup table. Consequently the DLL's code never needs patching at runtime to address the program's memory; the code already consults the DLL's lookup table, and it is that table which gets adjusted at runtime so it points at the functions and data.

Unix has just a single sort of library file (`.a`), and it gathers code drawn from a number of object files (`.o`). While linking to produce a shared object file (`.so`), the linker can run into an identifier whose definition it cannot locate. It then hunts through the object files held in the libraries, and on finding the identifier it pulls in the whole of that object file's code.

Windows offers two flavors of library — a static library and an import library, both bearing the `.lib` extension. The static kind resembles a Unix `.a` file, holding code that gets pulled in where needed. The import kind exists mostly to assure the linker that some identifier is valid and will turn up in the program once the DLL has loaded. The linker draws on what the import library tells it to assemble the lookup table for identifiers that the DLL itself does not carry. Linking an application or a DLL can spit out an import library, and that import library then has to feed every later DLL that leans on the symbols in the application or DLL.

Imagine you are putting together two dynamically loaded modules, B and C, that ought to draw on a shared chunk of code A. Under Unix you would *not* hand `A.a` to the linker when producing `B.so` and `C.so`, because doing so would embed it twice and leave B and C each carrying their own duplicate. Over on Windows, producing `A.dll` yields `A.lib` as well, and you *do* feed `A.lib` to the linker for both B and C. That `A.lib` holds no code at all; what it stores is merely the information consulted at runtime to reach A's code.

Reaching for an import library on Windows roughly parallels writing `import spam`: it opens up spam's names to you without minting a fresh copy. Linking against a library on Unix is closer to `from spam import *`, which does produce its own separate copy.

 Py_NO_LINK_LIB

Disables the automatic `#pragma`-driven linkage against the Python library that CPython's header files carry out on your behalf.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](a-cookbook-approach.md) · [Next source section](windows-dll-use-and-link-options.md)
