# Logical operators

#### Logical operators

The customary logical operators let you compare network objects. Their ordering goes by network address first and by net mask second.

#### Logical operators

The customary logical operators let you compare interface objects.

When testing equality (`==` and `!=`), two objects count as equal only if their IP address and their network both match. No interface ever tests equal to an address object or a network object.

Ordering (`<`, `>`, etc) follows a different set of rules. Interface objects and address objects sharing one IP version may be compared, with the address objects invariably sorting ahead of the interface objects. A pair of interface objects is judged first on their networks, and when those coincide, next on their IP addresses.

[Subject index](INDEX.md) · [Previous](operators.md) · [Continue](iteration.md) · [Continue](ipaddress-v4-int-to-packed-to-ipaddress-get-mixed-type-key.md)
