# Why was Python created in the first place?

### Why was Python created in the first place?

Below is a *very* short account of how the whole thing began, in Guido van Rossum's own words:

>

In the ABC group at CWI I gained substantial experience building an interpreted language, and that work taught me a great deal about how languages are designed. Plenty of Python's traits trace back to that, such as relying on indentation to group statements and including very-high-level data types (though Python handles all the specifics differently).

ABC had several things I disliked, yet it also offered features I genuinely valued. Patching the ABC language (or its implementation) to address my objections simply wasn't feasible — indeed, the inability to extend it ranked among its worst shortcomings. Having spent some time with Modula-2+, I conversed with those who designed Modula-3 and studied the Modula-3 report. From Modula-3 came the syntax and behavior governing exceptions, along with a few additional Python traits.

My work sat within the Amoeba distributed operating system group at CWI. Writing C programs or Bourne shell scripts was a poor way to handle system administration there, because Amoeba carried its own system call interface that the Bourne shell couldn't conveniently reach. Wrestling with error handling under Amoeba drove home for me just how vital exceptions are as a language feature.

It dawned on me that the gap could be closed by a scripting language whose syntax resembled ABC yet could tap into Amoeba's system calls. Building something tied exclusively to Amoeba struck me as unwise, so I concluded I needed a language extensible in a general way.

Over the 1989 Christmas holidays, with plenty of free time, I resolved to attempt it. Across the following year, still tinkering largely on my own clock, Python saw growing use inside the Amoeba project, and my colleagues' responses prompted me to fold in many early refinements.

By February 1991, a little more than a year into the work, I chose to post it to USENET. What followed is recorded in the `Misc/HISTORY` file.

[Subject index](INDEX.md)
