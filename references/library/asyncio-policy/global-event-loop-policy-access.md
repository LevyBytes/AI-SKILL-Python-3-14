# Getting and Setting the Policy

### Getting and Setting the Policy

You can use the functions below to read and assign the policy for the running process:

 asyncio.get_event_loop_policy()

Return the current process-wide policy.

Deprecated since version 3.14: Now deprecated, the `get_event_loop_policy()` function is slated to disappear in Python 3.16.

 asyncio.set_event_loop_policy(*policy*)

Set the current process-wide policy to *policy*.

If *policy* is set to `None`, the default policy is restored.

Deprecated since version 3.14: Now deprecated, the `set_event_loop_policy()` function is on track to be dropped in Python 3.16.

[Subject index](INDEX.md) · [Previous](policies.md) · [Continue](asyncio-abstracteventlooppolicy-class.md)
