# How do I find undefined g++ symbols __builtin_new or __pure_virtual?

### How do I find undefined g++ symbols __builtin_new or __pure_virtual?

Loading g++ extension modules dynamically means you have to rebuild Python, relink it through g++ (swap LINKCC in the Python Modules Makefile), and link your own extension module with g++ as well (for example, `g++ -shared -o mymodule.so mymodule.o`).

[Subject index](INDEX.md)
