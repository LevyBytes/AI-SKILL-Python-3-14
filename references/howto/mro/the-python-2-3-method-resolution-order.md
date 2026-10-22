# The Python 2.3 Method Resolution Order

# Mro

### The Python 2.3 Method Resolution Order

Note

What you're reading is a historical piece, included as an appendix alongside the official documentation. While the Method Resolution Order covered here first *appeared* in Python 2.3, it remains in use across the releases that followed – Python 3 among them.

By [Michele Simionato](https://www.phyast.pitt.edu/~micheles/).

Abstract:

*This write-up is aimed at Python programmers who'd like to get to grips with the C3 Method Resolution Order that Python 2.3 employs. It isn't a beginner's text, yet it teaches in a fairly hands-on way, with plenty of fully worked examples. Since I know of no other freely available document covering the same ground, I expect it will come in handy.*

Disclaimer:

>

*I'm giving this document to the Python Software Foundation, released under the Python 2.3 license. As is customary in such cases, let me caution the reader: what comes next* should *be accurate, but I extend no warranty whatsoever. Rely on it at your own risk and peril!*

Acknowledgments:

>

*Everyone on the Python mailing list who wrote in with encouragement. Paul Foley, who flagged a number of inaccuracies and prompted me to include the section on local precedence ordering. David Goodger, for assistance with the reStructuredText formatting. David Mertz, for help with the editing. And lastly Guido van Rossum, who eagerly placed this document on the official Python 2.3 home-page.*

[Subject index](INDEX.md) · [Following source context](the-beginning.md)
