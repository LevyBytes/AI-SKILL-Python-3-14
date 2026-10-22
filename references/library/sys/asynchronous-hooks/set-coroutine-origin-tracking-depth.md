# sys.set_coroutine_origin_tracking_depth

sys.set_coroutine_origin_tracking_depth(*depth*)

Lets you switch coroutine origin tracking on or off. With it switched on, a coroutine object’s `cr_origin` attribute holds a tuple made of (filename, line number, function name) tuples that trace where the coroutine object came into being, the latest call listed first. With it switched off, `cr_origin` is `None`.

Switch it on by handing in a *depth* value above zero; that fixes how many frames’ worth of information gets captured. Switch it off by giving *depth* a value of zero.

The setting applies on a per-thread basis.

Added in version 3.7.

Note

This function is included only provisionally (consult [**PEP 411**](https://peps.python.org/pep-0411/) for the specifics.) Reach for it strictly when debugging.

[API family](INDEX.md) · [sys context index](../INDEX.md).
