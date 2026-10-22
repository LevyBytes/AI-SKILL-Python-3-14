# turtledemo — Changes since Python 3.0

### Changes since Python 3.0

- The `Turtle` methods `shearfactor()`, `shapetransform()` and `get_shapepoly()` are new additions. As a result, the complete set of regular linear transforms is now on hand for transforming turtle shapes. `tiltangle()` gained extra functionality: it can now both read and set the tilt angle.

- The `Screen` method `onkeypress()` joined the lineup to complement `onkey()`. Because the latter ties actions to the key release event, an alias `onkeyrelease()` was added for it as well.

- The `Screen.mainloop` method was added, so the standalone `mainloop()` function is no longer required when working with `Screen` and `Turtle` objects.

- Two input methods joined the set: `Screen.textinput` and `Screen.numinput`. They pop up input dialogs and hand back strings and numbers respectively.

[Subject index](INDEX.md) · [Previous](changes-since-python-2-6.md) · [Owning module, declaration or section: turtledemo](turtledemo-demo-scripts.md)
