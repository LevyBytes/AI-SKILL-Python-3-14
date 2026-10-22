# An example dictionary-based configuration

### An example dictionary-based configuration

What follows is a sample logging configuration dictionary, lifted from the [documentation on the Django project](https://docs.djangoproject.com/en/stable/topics/logging/#configuring-logging). Handing this dictionary to [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) brings the configuration into effect:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'filters': ['special']
        }
    }
}

```

Further details on this configuration are available in the [relevant section](https://docs.djangoproject.com/en/stable/topics/logging/#configuring-logging) of the Django documentation.

[Subject index](INDEX.md) · [Previous source context](two-sender-outputs-and-interleaved-listener-output.md) · [Following source context](custom-log-rotation-namer-and-rotator.md)
