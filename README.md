# 18app-python-sdk
Python SDK for developing merchant applications which accept 18app vouchers

## Convertire certificato da P12 a Pem

```bash
openssl pkcs12 -in certificatop12.p12 -out certificato.pem
```

## Creare key file

```bash
openssl pkcs12 -in out.p12 -nodes -out private.key -nocerts
```