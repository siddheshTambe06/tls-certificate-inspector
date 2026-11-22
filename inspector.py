import ssl
import socket
from datetime import datetime, timezone

hostname = input("Enter website domain: ").strip()
port = 443

context = ssl.create_default_context()

try:
    with socket.create_connection((hostname, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:

            certificate = secure_sock.getpeercert()

            issuer = dict(x[0] for x in certificate["issuer"])
            subject = dict(x[0] for x in certificate["subject"])

            expiry = datetime.fromtimestamp(
                ssl.cert_time_to_seconds(certificate["notAfter"]),
                tz=timezone.utc
            )

            remaining = expiry - datetime.now(timezone.utc)

            print("\n===== TLS CERTIFICATE REPORT =====")
            print("Domain:", hostname)
            print("TLS version:", secure_sock.version())
            print("Cipher suite:", secure_sock.cipher()[0])
            print("Subject:", subject.get("commonName"))
            print("Issuer:", issuer.get("organizationName"))
            print("Valid from:", certificate["notBefore"])
            print("Expires:", certificate["notAfter"])
            print("Days remaining:", remaining.days)
            print("Certificate verification: PASSED")

            if remaining.days <= 7:
                print("Status: CRITICAL - Expiring soon")
            elif remaining.days <= 30:
                print("Status: WARNING - Renewal recommended")
            else:
                print("Status: VALID")

            print("==================================")

except ssl.SSLCertVerificationError as error:
    print("\nCertificate verification: FAILED")
    print("Reason:", error.verify_message)

except ssl.SSLError as error:
    print("TLS error:", error)

except socket.gaierror:
    print("Error: Domain could not be resolved.")

except socket.timeout:
    print("Error: Connection timed out.")

except OSError as error:
    print("Connection error:", error)
