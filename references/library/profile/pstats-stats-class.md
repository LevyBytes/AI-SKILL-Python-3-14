# profile: `pstats.Stats`

### The `Stats` Class

Analysis of the profiler data is done using the `Stats` class.

 *class *pstats.Stats(**filenames or profile*, *stream=sys.stdout*)

This class constructor builds a "statistics object" instance from a *filename* (or a list of filenames) or from a `Profile` instance. Output goes to the stream named by *stream*.

The file the constructor above selects must have come from the matching version of `profile` or `cProfile`. Specifically, there is *no* promise of file compatibility with future releases of this profiler, nor any compatibility with files made by other profilers, or by the same profiler run on a different operating system. Should you supply several files, all the statistics belonging to identical functions are merged, letting a single report show an overall view across several processes. Should extra files need merging with the data already held in a `Stats` object, the `add()` method is available.

In place of reading the profile data from a file, you can use a `cProfile.Profile` or `profile.Profile` object as the source of profile data.

`Stats` objects have the following methods:

[Subject index](INDEX.md) · [Previous](profile-profile-class-to-profile-profile-runcall.md) · [Continue](pstats-stats-strip-dirs-to-pstats-stats-print-callers.md)
