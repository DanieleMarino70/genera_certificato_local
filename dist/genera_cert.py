from OpenSSL import crypto
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

import os

def generate_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def generate_csr(key, common_name, organization, country, state, locality, organizational_unit, email):
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, email),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
    ])

    builder = x509.CertificateSigningRequestBuilder().subject_name(subject)

    # Add subjectAltName extension
    san = x509.SubjectAlternativeName([
        x509.DNSName("*.localhost"),
        x509.DNSName("localhost"),
    ])
    builder = builder.add_extension(san, critical=False)

    csr = builder.sign(key, algorithm=hashes.SHA256(), backend=default_backend())
    return csr

def generate_certificate(csr, key, folder_name, days_valid=365):
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(csr.subject)
    builder = builder.issuer_name(csr.subject)
    builder = builder.not_valid_before(datetime.now(timezone.utc))
    builder = builder.not_valid_after(datetime.now(timezone.utc) + timedelta(days=days_valid))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(csr.public_key())

    builder = builder.add_extension(
        x509.BasicConstraints(ca=False, path_length=None), critical=True,
    )

    # Extract the SubjectAlternativeName extension from the CSR and add it to the certificate
    san_extension = csr.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
    builder = builder.add_extension(san_extension.value, critical=False)

    builder = builder.add_extension(
        x509.SubjectKeyIdentifier.from_public_key(csr.public_key()), critical=False,
    )

    # Add the SubjectKeyIdentifier extension directly from the key
    builder = builder.add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_subject_key_identifier(
            x509.SubjectKeyIdentifier.from_public_key(key.public_key())
        ),
        critical=False,
    )

    cert = builder.sign(key, hashes.SHA256(), default_backend())

    # Save the private key
    private_key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    save_to_file(folder_name, "private.key", private_key_pem)

    # Save the certificate
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
    save_to_file(folder_name, "certificate.crt", cert_pem)

    return cert

def save_to_file(folder, filename, data):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, filename), "wb") as file:
        file.write(data)

# Default values
default_values = {
    "common_name": "localhost",
    "organization": "IT",
    "country": "US",
    "state": "KS",
    "locality": "Olathe",
    "organizational_unit": "IT Department",
    "email": "webmaster@example.com"
}

# Function to modify default values
def modify_default_values():
    # Now the default_values dictionary is updated based on user input
    print("Default values:", default_values)
    print("Modify default values:")
    for key in default_values:
        new_value = input(f"Enter new {key} (press Enter to keep default value '{default_values[key]}'): ")
        if new_value:
            default_values[key] = new_value
    return default_values

def main():
    try:
        # Call the function to modify default values
        modify_default_values()

        # Update values based on user input
        common_name = default_values['common_name']
        organization = default_values['organization']
        country = default_values['country']
        state = default_values['state']
        locality = default_values['locality']
        organizational_unit = default_values['organizational_unit']
        email = default_values['email']

        # Specify the path to the "certificati" folder at the project root level
        certificati_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "certificati")

        # Construct the folder path inside "certificati"
        folder_name = os.path.join(certificati_folder, "certificazione-" + common_name)

        # Genera la chiave privata e la CSR come hai fatto prima
        key = generate_key()
        csr = generate_csr(
            key,
            common_name=common_name,
            organization=organization,
            country=country,
            state=state,
            locality=locality,
            organizational_unit=organizational_unit,
            email=email
        )

        # Genera il certificato a partire dalla CSR e dalla chiave privata
        cert = generate_certificate(csr, key, folder_name)  # Pass the folder_name here
        print("Certificate generation successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
