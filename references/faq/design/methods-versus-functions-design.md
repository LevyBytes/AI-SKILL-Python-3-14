# Why does Python use methods for some functionality (e.g. list.index()) but functions for other (e.g. len(list))?

### Why does Python use methods for some functionality (e.g. list.index()) but functions for other (e.g. len(list))?

In Guido's words:

>

(a) For certain operations, prefix notation simply reads better than postfix ? prefix (and infix!) operations carry a long mathematical tradition that favors notations whose visuals aid the mathematician's thinking about a problem. Contrast the ease with which we recast a formula such as x*(a+b) into x*a + x*b against the awkwardness of achieving the same with raw OO notation.

(b) Whenever I read code that says len(x) I *know* it's requesting the length of something. That conveys two facts to me: the result is an integer, and the argument is some sort of container. Conversely, reading x.len() obliges me to already know that x is a kind of container implementing an interface or inheriting from a class equipped with a standard len(). Consider the confusion that crops up every so often when a class not implementing a mapping carries a get() or keys() method, or when something that is no file has a write() method.

?[https://mail.python.org/pipermail/python-3000/2006-November/004643.html](https://mail.python.org/pipermail/python-3000/2006-November/004643.html)

[Subject index](INDEX.md)
