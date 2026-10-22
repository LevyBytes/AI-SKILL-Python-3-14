# sys.__breakpointhook__, sys.__displayhook__, sys.__excepthook__, sys.__unraisablehook__

sys.__breakpointhook__

sys.__displayhook__

sys.__excepthook__

sys.__unraisablehook__

These objects hold the starting values of `breakpointhook`, `displayhook`, `excepthook`, and `unraisablehook` from the moment the program began. They are kept around so that `breakpointhook`, `displayhook` and `excepthook`, `unraisablehook` can be reinstated should they ever be swapped out for broken or alternative objects.

Added in version 3.7: __breakpointhook__

Added in version 3.8: __unraisablehook__

[API family](INDEX.md) · [sys context index](../INDEX.md).
