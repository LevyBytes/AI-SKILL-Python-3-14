# Python 3.7.0 beta 2 / library / functions and types

[bpo-32929](https://bugs.python.org/issue?@action=redirect&bpo=32929): Drop the three-state parameter "hash", while adding the boolean "unsafe_hash". When unsafe_hash is True, a __hash__ function gets added, yet whenever a __hash__ already exists, TypeError is raised. When unsafe_hash is False, a __hash__ is added derived from the values of eq= and frozen=. The unsafe_hash=False behavior matches the former hash=None behavior. unsafe_hash=False acts as the default, exactly as hash=None did previously.

[bpo-32859](https://bugs.python.org/issue?@action=redirect&bpo=32859): Within `os.dup2`, avoid checking on every call whether the `dup3` syscall is present.

[bpo-32741](https://bugs.python.org/issue?@action=redirect&bpo=32741): Add the `asyncio.TimerHandle.when()` method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
