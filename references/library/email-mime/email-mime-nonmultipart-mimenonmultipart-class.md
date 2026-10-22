# email.mime — `email.mime`: Creating email and MIME objects from scratch

*class *email.mime.nonmultipart.MIMENonMultipart

Module: `email.mime.nonmultipart`

Derived from `MIMEBase`, this stands as an intermediate base class covering MIME messages that are not *multipart*. The chief reason this class exists is to block use of the [`attach()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) method, which is only meaningful for *multipart* messages. Calling `attach()` triggers a [`MultipartConversionError`](https://docs.python.org/3.14/library/email.errors.html#email.errors.MultipartConversionError) exception.

[Subject index](INDEX.md) · [Previous](email-mime-base-mimebase-class.md) · [Continue](email-mime-multipart-mimemultipart-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
