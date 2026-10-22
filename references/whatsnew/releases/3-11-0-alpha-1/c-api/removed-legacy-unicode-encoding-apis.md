# Python 3.11.0 alpha 1 / c api / removed legacy unicode encoding apis

[bpo-44029](https://bugs.python.org/issue?@action=redirect&bpo=44029): Drop the deprecated `Py_UNICODE` APIs: `PyUnicode_Encode`, `PyUnicode_EncodeUTF7`, `PyUnicode_EncodeUTF8`, `PyUnicode_EncodeUTF16`, `PyUnicode_EncodeUTF32`, `PyUnicode_EncodeLatin1`, `PyUnicode_EncodeMBCS`, `PyUnicode_EncodeDecimal`, `PyUnicode_EncodeRawUnicodeEscape`, `PyUnicode_EncodeCharmap`, `PyUnicode_EncodeUnicodeEscape`, `PyUnicode_TransformDecimalToASCII`, `PyUnicode_TranslateCharmap`, `PyUnicodeEncodeError_Create`, `PyUnicodeTranslateError_Create`. Consult [**PEP 393**](https://peps.python.org/pep-0393/) and [**PEP 624**](https://peps.python.org/pep-0624/) for details.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
