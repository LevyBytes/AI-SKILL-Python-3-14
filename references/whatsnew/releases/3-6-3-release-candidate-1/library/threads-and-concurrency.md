# Python 3.6.3 release candidate 1 / library / threads and concurrency

[bpo-29212](https://bugs.python.org/issue?@action=redirect&bpo=29212): Correct concurrent.futures.thread.ThreadPoolExecutor threads so that, by default, their thread name is not based on repr() whenever no thread_name_prefix has been provided. From now on they identify as ?ThreadPoolExecutor-y_n?.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
