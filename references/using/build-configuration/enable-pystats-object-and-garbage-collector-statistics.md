# --enable-pystats object and garbage-collector statistics

- Object:

  - incref and decref;

  - interpreter incref and decref;

  - allocations: all, 512 bytes, 4 kiB, big;

  - free;

  - to/from free lists;

  - dictionary materialized/dematerialized;

  - type cache;

  - optimization attempts;

  - optimization traces created/executed;

  - uops executed.

- Garbage collector:

  - Garbage collections;

  - Objects visited;

  - Objects collected.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source section](enable-pystats-opcode-and-call-statistics.md) · [Following source section](disable-gil.md) · [Enable and collect statistics](enable-pystats.md) · [Opcode and call statistics](enable-pystats-opcode-and-call-statistics.md)
