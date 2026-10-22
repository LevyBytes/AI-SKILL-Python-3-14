# What kinds of global value mutation are thread-safe?

### What kinds of global value mutation are thread-safe?

Internally, a [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL) guarantees that just one thread executes inside the Python VM at any moment. Generally, Python permits thread switching only at the boundaries between bytecode instructions; the switching frequency is adjustable through [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval). Consequently every bytecode instruction — and thus all of the C implementation code it reaches — is atomic as far as a Python program can tell.

Theoretically, then, a precise accounting demands a precise grasp of the PVM bytecode implementation. As a working rule, operations touching shared variables whose built-in data types (ints, lists, dicts, etc) ?look atomic? genuinely are.

For instance, each operation listed below is atomic (here L, L1, L2 denote lists; D, D1, D2 denote dicts; x, y denote objects; i, j denote ints):

```python
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop()
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()

```

These aren't:

```python
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1

```

When an operation displaces other objects, it can trigger those objects? [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method once their reference count hits zero, and that may have side effects. Bulk updates to dictionaries and lists are especially prone to this. Whenever you're unsure, reach for a mutex!

[Subject index](INDEX.md)
