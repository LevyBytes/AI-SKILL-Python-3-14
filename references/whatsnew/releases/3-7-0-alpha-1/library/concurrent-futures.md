# Python 3.7.0 alpha 1 / library / concurrent futures

[bpo-27144](https://bugs.python.org/issue?@action=redirect&bpo=27144): The `map()` and `as_completed()` iterators within `concurrent.futures` no longer hold onto a reference to the objects they yield.

[bpo-31249](https://bugs.python.org/issue?@action=redirect&bpo=31249): concurrent.futures: the WorkItem.run() method that ThreadPoolExecutor uses now severs a reference cycle linking an exception object with the WorkItem object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
