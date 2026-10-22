# Python 3.5.0 alpha 1 / library / memory and lifetimes

[bpo-22166](https://bugs.python.org/issue?@action=redirect&bpo=22166): Backed by a fresh internal _codecs._forget_codec helper function, test_codecs now flushes the encoding caches so that no apparent reference leak surfaces

[bpo-22003](https://bugs.python.org/issue?@action=redirect&bpo=22003): When seeded from a bytes object, io.BytesIO() now puts off copying until a mutation occurs, which improves speed and memory footprint in certain scenarios. David Wilson wrote the patch.

[bpo-21529](https://bugs.python.org/issue?@action=redirect&bpo=21529): Corrected an arbitrary memory access within JSONDecoder.raw_decode whenever the second parameter is negative. Guido Vranken reported this bug. (See also: [**CVE 2014-4616**](https://www.cve.org/CVERecord?id=CVE-2014-4616))

[bpo-22448](https://bugs.python.org/issue?@action=redirect&bpo=22448): Cleanup of canceled timer handles was improved to head off unbound memory usage. Joshua Moore-Oliva supplied the patch.

[bpo-21951](https://bugs.python.org/issue?@action=redirect&bpo=21951): When memory allocation fails, Tkinter now most likely raises MemoryError rather than crashing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
