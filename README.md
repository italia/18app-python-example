# 18app-python-sdk

Esempio in Python per sviluppare applicazioni che accettano i vouchers 18app

⚠️ Attenzione! Questo progetto non è attivamente sviluppato e manutenuto. Se vuoi contribuire al progetto e diventare maintainer contattaci sul [canale Slack dedicato](https://developersitalia.slack.com/archives/C7AAA10PN) .

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
