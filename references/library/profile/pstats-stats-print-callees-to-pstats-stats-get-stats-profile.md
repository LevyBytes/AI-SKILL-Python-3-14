# profile: `print_callees()`, `get_stats_profile()`

print_callees(**restrictions*)

This `Stats` class method prints a list of every function that the indicated function called. Apart from reversing the direction of the calls (re: called vs was called by), the arguments and ordering match those of the `print_callers()` method.

 get_stats_profile()

This method returns a StatsProfile instance, which holds a mapping from function names to FunctionProfile instances. Every FunctionProfile instance keeps details about that function's profile, like the run time of the function, the number of times it was called, and so forth.

Added in version 3.9: The following dataclasses were added: StatsProfile, FunctionProfile. The following function was added: get_stats_profile.

[Subject index](INDEX.md) · [Previous](pstats-stats-strip-dirs-to-pstats-stats-print-callers.md) · [Continue](what-is-deterministic-profiling.md) · [Owning module, declaration or section: pstats.Stats](pstats-stats-class.md) · [Owning module, declaration or section: The `Stats` Class](pstats-stats-class.md)
