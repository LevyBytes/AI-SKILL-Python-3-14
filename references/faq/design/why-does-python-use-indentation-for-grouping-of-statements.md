# Why does Python use indentation for grouping of statements?

### Design and History FAQ

### Why does Python use indentation for grouping of statements?

In Guido van Rossum's view, grouping by indentation is remarkably elegant and adds greatly to how readable a typical Python program turns out to be. After some time with it, the majority of people come to appreciate the feature.

With no begin/end brackets present, there is no room for the grouping seen by the parser to diverge from what a human reader perceives. Now and then a C programmer runs across a snippet that looks like this:

```python
if (x <= y)
        x++;
        y--;
z++;

```

Here, only the `x++` statement runs when the test holds, yet the indentation misleads many into thinking the opposite. Even seasoned C programmers may gaze at this for a while, puzzled over why `y` gets decremented even in the `x > y` case.

Lacking begin/end brackets, Python is far less subject to clashes over coding style. C offers numerous ways to position the braces. Once you've grown accustomed to reading and writing in one chosen style, it's normal to feel a little ill at ease when reading (or being asked to write) in another.

Plenty of coding styles set begin/end brackets on their own separate line. That stretches programs out noticeably and squanders precious screen space, which makes it tougher to grasp the whole of a program at a glance. In an ideal case, a function ought to fit on a single screen (say, 20–30 lines). 20 lines of Python accomplishes considerably more than 20 lines of C. The credit isn't owed only to the absence of begin/end brackets ? the missing declarations and the high-level data types play their part too ? yet the indentation-driven syntax assuredly contributes.

[Subject index](INDEX.md)
