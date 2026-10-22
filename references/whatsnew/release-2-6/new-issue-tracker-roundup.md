# What’s New in Python 2.6 / New Issue Tracker: Roundup

### New Issue Tracker: Roundup

Over a long stretch, frustration with SourceForge’s bug tracker had been mounting among the Python developers. Because SourceForge runs a hosted offering, there’s little room to tailor it; as one example, reshaping the life cycle of an issue simply couldn’t be done.

That led the infrastructure committee of the Python Software Foundation to put out a request for issue trackers, inviting volunteers to stand up various products and pull in a sample of the bugs and patches from SourceForge. The group reviewed four trackers in all: [Jira](https://www.atlassian.com/software/jira/), [Launchpad](https://launchpad.net/), [Roundup](https://roundup.sourceforge.io/), and [Trac](https://trac.edgewall.org/). In the end the committee narrowed the field to two finalists, Jira and Roundup. Jira is sold commercially but hands free-software projects hosted instances at no charge; Roundup is open source, needing volunteers to run it plus a server on which to host it.

Once a request for volunteers went out, a fresh Roundup deployment came online at [https://bugs.python.org](https://bugs.python.org). Since a single Roundup deployment can run several trackers, that same server now also carries issue trackers for Jython and the Python web site. No doubt more uses will come along later. Wherever it can, this edition of “What’s New in Python” points to the bug/patch entry behind each change.

The Python bug tracker is graciously hosted by [Upfront Systems](https://upfrontsoftware.co.za), based in Stellenbosch, South Africa. Martin von Löwis devoted considerable work to bringing across the existing bugs and patches out of SourceForge; the scripts he used for that import live at `https://svn.python.org/view/tracker/importer/` and might help other projects looking to migrate off SourceForge onto Roundup.

See also

[https://bugs.python.org](https://bugs.python.org)

The Python bug tracker.

[https://bugs.jython.org](https://bugs.jython.org):

The Jython bug tracker.

[https://roundup.sourceforge.io/](https://roundup.sourceforge.io/)

Roundup downloads and documentation.

[https://svn.python.org/view/tracker/importer/](https://svn.python.org/view/tracker/importer/)

Martin von Löwis’s conversion scripts.

[Subject index](INDEX.md) · [Previous source section](changes-to-the-development-process.md) · [Next source section](new-documentation-format-restructuredtext-using-sphinx.md) · [Release/subject declaration](python-3-0.md)
