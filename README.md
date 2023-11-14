# Generatore di Certificati

Questo progetto Python consente di generare chiavi private, richieste di certificato (CSR), e certificati autofirmati utilizzando la libreria OpenSSL.

## Istruzioni

1. **Clona il repository o copia i file nel tuo progetto.**
2. **Assicurati di avere Python installato sul tuo sistema.**
3. **Installazione delle dipendenze:**
   
    ```bash
    pip install pyopenssl
    ```

4. **Esecuzione dello script:**
   
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

## Nota

Questo script genera certificati autofirmati, adatti solo a scopi di sviluppo o testing. Per ambienti di produzione, è consigliabile ottenere certificati da un'autorità di certificazione affidabile.

Buona generazione di certificati!

Made with :sparkling_heart: da [@Daniele Marino](https://github.com/DanieleMarino70)