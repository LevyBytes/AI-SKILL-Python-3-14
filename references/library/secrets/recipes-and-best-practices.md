# secrets — Recipes and best practices

### Recipes and best practices

In this section you will find recipes and best practices for putting `secrets` to work to manage a basic level of security.

Generate an eight-character alphanumeric password:

```python
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

```

Note

Applications should not [**store passwords in a recoverable format**](https://cwe.mitre.org/data/definitions/257.html), be it plain text or encrypted. Instead, salt them and run them through a cryptographically strong one-way (irreversible) hash function.

Generate a ten-character alphanumeric password holding a minimum of one lowercase letter, one uppercase letter, and three digits:

```python
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

```

Generate an [XKCD-style passphrase](https://xkcd.com/936/):

```python
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))

```

Generate a hard-to-guess temporary URL that carries a security token fit for password recovery applications:

```python
import secrets
url = 'https://example.com/reset=' + secrets.token_urlsafe()

```

[Subject index](INDEX.md) · [Previous](secrets-compare-digest.md) · [Continue](../security-warnings/security-considerations.md) · [Owning module, declaration or section: secrets](secrets-generate-secure-random-numbers-for-managing-secrets.md)
