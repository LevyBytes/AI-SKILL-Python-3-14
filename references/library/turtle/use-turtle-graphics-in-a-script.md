# Use turtle graphics in a script

### Use turtle graphics in a script

The advice is to lean on the `turtle` module namespace just covered above, for instance:

```python
import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

```

There's one more thing to handle, though ? the moment your script finishes, Python will likewise shut the turtle's window. Append:

```python
t.mainloop()

```

at the script's end. From then on the script holds open, awaiting dismissal, and won't quit until something ends it ? for example, when you close the turtle graphics window.

[Subject index](INDEX.md) · [Previous](use-the-turtle-module-namespace.md) · [Continue](use-object-oriented-turtle-graphics.md)
