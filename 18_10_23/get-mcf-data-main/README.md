# get-mcf-data
Strumenti per scaricare i dati relativi al corso di Metodi Computazionali per la Fisica

Prerequisiti:
* modulo _argparse_

`get_data.py` scarica i file per le esercitazioni. Ogni esercitazione separatamente.


E' necessario specificare l'anno di corso a cui si fa riferimento con l'opzione `--year`
Attualmente i valori possibili sono:
- 2022
- 2023

E' necessario specificare l'esercitazione per cui si vogliono scaricare i dati tramite l'opzione  `--exn`

Si può specificare una cartella di destinazione 

  Per informazioni su uso ed opzioni:
  >python3 get_data.py --help



  Esempio:
  >python3 get_data.py --year 2023  --exn 5


  Esempio con cartella di destinazione:
  >python3 get_data.py --year 2023  --exn 5  --outdir ./ex5_data





