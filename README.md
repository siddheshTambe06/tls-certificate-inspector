
# TLS Certificate Inspector

A lightweight Python tool for inspecting and validating TLS certificates presented by HTTPS websites.

## Features

- TLS certificate verification
- Certificate subject and issuer extraction
- Certificate expiry monitoring
- Expiry warnings at 30 and 7 days
- Negotiated TLS version and cipher suite identification
- Hostname mismatch detection
- Expired and untrusted certificate detection
- DNS and connection error handling

## Technologies

- Python 3.9
- SSL/TLS
- Socket programming
- X.509 certificates
- Public Key Infrastructure (PKI)

## Usage

Run the following command:

```bash
python3 inspector.py
```

Enter a website domain when prompted.

## Security Testing

The tool was successfully tested against seven scenarios, including valid, expired, self-signed and untrusted certificates, hostname mismatches and DNS failures.

## Security Design

Certificate verification remains enabled throughout. The tool does not bypass certificate trust or hostname validation.

## Author

Siddhesh Yadav Tambe

