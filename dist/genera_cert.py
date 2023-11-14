from OpenSSL import crypto
from datetime import datetime, timedelta
import os

def generate_key():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)
    return key

def generate_csr(key, common_name, organization):
    req = crypto.X509Req()
    req.get_subject().CN = common_name
    req.get_subject().O = organization
    req.set_pubkey(key)
    req.sign(key, "sha256")
    return req

def generate_certificate(csr, key, days_valid=365):
    cert = crypto.X509()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(days_valid * 24 * 60 * 60)
    cert.set_issuer(csr.get_subject())
    cert.set_subject(csr.get_subject())
    cert.set_pubkey(csr.get_pubkey())
    cert.sign(key, "sha256")
    return cert

def save_to_file(folder, filename, data):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, filename), "wb") as file:
        file.write(data)

def main():
    namecom = input("Inserisci il nome comune: ")
    org = input("Inserisci il nome dell'organizzazione: ")
    
    # Specify the path to the "certificati" folder at the project root level
    certificati_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "certificati")
    
    # Construct the folder path inside "certificati"
    folder_name = os.path.join(certificati_folder, "certificazione-" + namecom)

    # Genera la chiave privata e la CSR come hai fatto prima
    key = generate_key()
    csr = generate_csr(key, namecom, org)

    # Genera il certificato a partire dalla CSR e dalla chiave privata
    cert = generate_certificate(csr, key)

    # Salva la chiave privata, la CSR e il certificato nella cartella specificata
    save_to_file(folder_name, "private.key", crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    save_to_file(folder_name, "request.csr", crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr))
    save_to_file(folder_name, "certificate.crt", crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

if __name__ == "__main__":
    main()
    namecom = input("Inserisci il nome comune: ")
    org = input("Inserisci il nome dell'organizzazione: ")
    
    # Specify the path to the "certificati" folder at the project root level
    certificati_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "certificati")

    folder_name = os.path.join(parent_directory, "certificazione-" + namecom)

    # Genera la chiave privata e la CSR come hai fatto prima
    key = generate_key()
    csr = generate_csr(key, namecom, org)

    # Genera il certificato a partire dalla CSR e dalla chiave privata
    cert = generate_certificate(csr, key)

    # Salva la chiave privata, la CSR e il certificato nella cartella specificata
    save_to_file(folder_name, "private.key", crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    save_to_file(folder_name, "request.csr", crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr))
    save_to_file(folder_name, "certificate.crt", crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

if __name__ == "__main__":
    main()
