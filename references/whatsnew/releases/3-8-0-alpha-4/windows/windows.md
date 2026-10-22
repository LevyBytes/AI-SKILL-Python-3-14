# Python 3.8.0 alpha 4 / windows / windows

[bpo-35941](https://bugs.python.org/issue?@action=redirect&bpo=35941): The ssl module's enum_certificates function now pulls certificates from every certificate store reachable inside windows within a single query, rather than handing back only the ones held in the system wide certificate store. The certificate stores covered are:

> local machine
> local machine enterprise
> local machine group policy
> current user
> current user group policy
> services
> users

The ssl.enum_crls() function received the equivalent treatment, so it returns every certificate revocation list found across the windows certificate revocation list stores.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
