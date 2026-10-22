# Python 3.14 changes: Asyncio task-tree output and await cycles

```bash
python -m asyncio pstree 12345

└── (T) Task-1
    └──  main example.py:13
        └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
            └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                ├── (T) Sundowning
                │   └──  album example.py:8
                │       └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
                │           └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                │               ├── (T) TNDNBTG
                │               │   └──  play example.py:4
                │               │       └──  sleep Lib/asyncio/tasks.py:702
                │               └── (T) Levitate
                │                   └──  play example.py:4
                │                       └──  sleep Lib/asyncio/tasks.py:702
                └── (T) TMBTE
                    └──  album example.py:8
                        └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
                            └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                                ├── (T) DYWTYLM
                                │   └──  play example.py:4
                                │       └──  sleep Lib/asyncio/tasks.py:702
                                └── (T) Aqua Regia
                                    └──  play example.py:4
                                        └──  sleep Lib/asyncio/tasks.py:702

```

Should a cycle turn up in the async await graph (a possible sign of a programming defect), the tool throws an error and enumerates the cycle paths that block tree construction:

```bash
python -m asyncio pstree 12345

ERROR: await-graph contains cycles - cannot print a tree!

cycle: Task-2 → Task-3 → Task-2

```

[Subject index](INDEX.md) · [Previous source section](asyncio-introspection-capabilities.md) · [Next source section](concurrent-safe-warnings-control.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](asyncio-introspection-capabilities.md)
