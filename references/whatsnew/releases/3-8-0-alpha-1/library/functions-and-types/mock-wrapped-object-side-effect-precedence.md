# Python 3.8.0 alpha 1 / library / whenever mock instance wraps object if side effect supplied one

[bpo-35330](https://bugs.python.org/issue?@action=redirect&bpo=35330): Whenever a `Mock` instance wraps an object, if `side_effect` is supplied on one of that object's mocked methods, skip the original implementation and hand back the side effect result exactly the way it works with return_value.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
