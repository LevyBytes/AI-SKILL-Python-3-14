# Why does Python sometimes take so long to start?

### Why does Python sometimes take so long to start?

As a rule Python launches almost instantly on Windows, yet every so often bug reports surface in which Python abruptly starts taking ages to come up. The puzzle deepens because that same Python runs perfectly well on other Windows machines that look configured the very same way.

The culprit could well be misconfigured virus-checking software on the troublesome machine. Certain virus scanners have been observed to pile on startup overhead of two orders of magnitude once the scanner is set to watch every read from the filesystem. Inspect the virus-scanning software's settings across your machines to confirm they really are configured the same. McAfee, set to scan all file system read activity, stands out as one notable offender.

[Subject index](INDEX.md)
