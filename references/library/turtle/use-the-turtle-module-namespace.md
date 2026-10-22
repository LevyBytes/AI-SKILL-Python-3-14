# Use the `turtle` module namespace

### Use the `turtle` module namespace

While `from turtle import *` is handy, take note that it brings in a sizeable batch of objects, so unless you're strictly doing turtle graphics you risk colliding names (a hazard that grows when turtle graphics runs inside a script that might import additional modules).

The fix is to write `import turtle` ? now `fd()` turns into `turtle.fd()`, `width()` turns into `turtle.width()`, and likewise for the rest. (Should spelling out ?turtle? repeatedly grow tiresome, try something like `import turtle as t` instead.)

[Subject index](INDEX.md) · [Previous](automatically-begin-and-end-filling.md) · [Continue](use-turtle-graphics-in-a-script.md)
