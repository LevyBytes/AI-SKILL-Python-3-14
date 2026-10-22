# Python 3.6.3 release candidate 1 / library / concurrent futures

[bpo-27144](https://bugs.python.org/issue?@action=redirect&bpo=27144): Within `concurrent.futures`, the `map()` and `as_completed()` iterators now refrain from holding a reference to objects they yield.

[bpo-31249](https://bugs.python.org/issue?@action=redirect&bpo=31249): concurrent.futures: the WorkItem.run() method that ThreadPoolExecutor invokes now severs a reference cycle linking an exception object and the WorkItem object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
