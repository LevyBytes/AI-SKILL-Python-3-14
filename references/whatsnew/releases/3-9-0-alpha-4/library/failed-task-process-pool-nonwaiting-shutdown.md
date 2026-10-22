# Python 3.9.0 alpha 4 / library / fix hanging processpoolexcutor shutdown wait false whenever task failed

[bpo-39104](https://bugs.python.org/issue?@action=redirect&bpo=39104): Fix a hanging ProcessPoolExcutor on `shutdown(wait=False)` whenever a task has failed to pickle.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
