# 18app-python-example

Esempio in Python per sviluppare applicazioni che accettano i vouchers 18app

⚠️ Attenzione! Questo progetto non è più manutenuto dai suoi autori. Se vuoi contribuire al progetto e diventare maintainer contattaci sul [canale Slack](https://developersitalia.slack.com/archives/C7AAA10PN) dedicato.

## Setup

```bash
pip install -r requirements.txt
```

Per lanciare i test

```bash
python int_tests.py
```

## Utilities

- Convertire certificato da P12 a Pem

```bash
openssl pkcs12 -in certificatop12.p12 -out certificato.pem
```

- Creare key file

```bash
openssl pkcs12 -in out.p12 -nodes -out private.key -nocerts
```
