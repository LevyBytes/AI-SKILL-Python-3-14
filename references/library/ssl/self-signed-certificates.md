# ssl - Self-signed certificates

### Self-signed certificates

Should you set out to build a server offering SSL-encrypted connection services, you will have to obtain a certificate for that service. Certificates can be obtained through numerous routes, for instance by purchasing one from a certification authority. A frequent alternative is to produce a self-signed certificate. Generating one is easiest with the OpenSSL package, by running something along these lines:

```python
% openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
Generating a 1024 bit RSA private key
.......++++++
.............................++++++
writing new private key to 'cert.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:MyState
Locality Name (eg, city) []:Some City
Organization Name (eg, company) [Internet Widgits Pty Ltd]:My Organization, Inc.
Organizational Unit Name (eg, section) []:My Group
Common Name (eg, YOUR name) []:myserver.mygroup.myorganization.com
Email Address []:ops@myserver.mygroup.myorganization.com
%

```

A self-signed certificate carries the drawback that it serves as its own root certificate, so nobody else will hold it among their stash of recognized (and trusted) root certificates.

[Subject index](INDEX.md) · [Previous](combined-key-and-certificate.md) · [Continue](testing-for-ssl-support.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
