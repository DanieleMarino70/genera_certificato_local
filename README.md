# Generatore di Certificati

Questo progetto Python consente di generare chiavi private, richieste di certificato (CSR), e certificati autofirmati utilizzando la libreria OpenSSL tramite file conf.

## Istruzioni

1. **Clona il repository o copia i file nel tuo progetto.**
2. **Assicurati di avere Python installato sul tuo sistema e Git**
3. **Installazione delle dipendenze:**
4. **Modifica del file openssl-custom.cnf**
    *modifiche da non effettuare contrassegnate con X*
    ```bash 
        [req]
        default_bits = 2048 - X
        prompt = no - X
        default_md = sha256 - X
        x509_extensions = v3_req - X
        distinguished_name = dn - X

        [dn]
        C = US
        ST = KS
        L = Olathe
        O = IT
        OU = IT Department
        emailAddress = webmaster@example.com
        CN = localhost

        [v3_req]
        subjectAltName = @alt_names

        [alt_names]
        DNS.1 = *.localhost - X
        DNS.2 = localhost - X
    ```
  

5. **Esecuzione dello script:**
   
    ```bash
    python genera_cert.py
    ```
    oppure da:

    ```bash
    run_genera_cert.bat
    ``` 

    Segui le istruzioni per inserire il nome comune e l'organizzazione per generare i certificati nella cartella `certificati`.

## Struttura del Progetto

- `genera_cert.py`: Lo script principale per la generazione di chiavi private, CSR, e certificati.
- `certificati/`: La cartella in cui vengono salvati i certificati generati.

## Istruzioni
```bash
OS X
	1. Double click on the certificate (server.crt)
	2. Select your desired keychain (login should suffice)
	3. Add the certificate
	4. Open Keychain Access if it isn’t already open
	5. Select the keychain you chose earlier
	6. You should see the certificate localhost
	7. Double click on the certificate
	8. Expand Trust
	9. Select the option Always Trust in When using this certificate
	10. Close the certificate window

The certificate is now installed.


Windows 10

	1. Double click on the certificate (server.crt)
	2. Click on the button “Install Certificate …”
	3. Select whether you want to store it on user level or on machine level
	4. Click “Next”
	5. Select “Place all certificates in the following store”
	6. Click “Browse”
	7. Select “Trusted Root Certification Authorities”
	8. Click “Ok”
	9. Click “Next”
	10. Click “Finish”

If you get a prompt, click “Yes”
```
## Nota

Questo script genera certificati autofirmati, adatti solo a scopi di sviluppo o testing. Per ambienti di produzione, è consigliabile ottenere certificati da un'autorità di certificazione affidabile.



Buona generazione di certificati!

Made with :sparkling_heart: da [@Daniele Marino](https://github.com/DanieleMarino70)
