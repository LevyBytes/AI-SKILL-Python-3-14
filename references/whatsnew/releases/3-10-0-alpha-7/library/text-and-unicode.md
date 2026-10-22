# Python 3.10.0 alpha 7 / library / text and unicode

[bpo-27820](https://bugs.python.org/issue?@action=redirect&bpo=27820): Patched a long-standing smtplib.SMTP defect where running AUTH LOGIN with initial_response_ok=False ended in failure.

The root cause: SMTP.auth_login _always_ hands back a password whenever it is given a challenge string, which violates the AUTH LOGIN standard.

This also repairs a defect in the test covering smtpd.

[bpo-43125](https://bugs.python.org/issue?@action=redirect&bpo=43125): When base64mime.body_encode is handed empty bytes, return an empty string

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
