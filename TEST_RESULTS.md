
# TLS Certificate Inspector - Test Results

## Test Environment

- Date: 22 November 2026
- Operating system: macOS
- Python version: 3.9.6
- HTTPS port: 443
- Certificate verification: Enabled

## Test Results

| Test Domain | Scenario | Actual Result | Status |
|---|---|---|---|
| google.com | Valid certificate | Verified successfully | PASS |
| github.com | Valid certificate | Verified successfully | PASS |
| expired.badssl.com | Expired certificate | Certificate expired | PASS |
| self-signed.badssl.com | Self-signed certificate | Certificate rejected | PASS |
| wrong.host.badssl.com | Hostname mismatch | Certificate rejected | PASS |
| untrusted-root.badssl.com | Untrusted root CA | Certificate chain rejected | PASS |
| example.invalid | Invalid domain | DNS resolution failure handled | PASS |

## Summary

- Total manual tests: 7
- Passed: 7
- Failed: 0
- Test success rate: 100%

## Conclusion

The application successfully handled all seven
tested scenarios without disabling certificate
verification or hostname validation.

These results demonstrate the behaviour of the
tool under the tested conditions.

