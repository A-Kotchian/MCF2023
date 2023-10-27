from datetime import datetime, timedelta



print("Benvenuto nel calcolatore di età!\n")

a=input("Inserisci l'anno,il mese,il giorno,l'ora,il minuto e i secondi di nascita nel formato:\n(Giorno-mese-Anno Ora:Min:Sec con - e :)\n")
if(a.find(":")==-1 or a.find("-")==-1):
    print("---------------------------------------------")
    print("\nFormato non valido,chiusura del programma\n")
    print("---------------------------------------------")
else:
    a=a.split(" ")
    b=a[0].split("-")
    c=a[1].split(":")


    anno=int(b[2])
    mese=int(b[1])
    giorno=int(b[0])
    ora=int(c[0])
    minuto=int(c[1])
    secondi=int(c[2])
    secondi_tot=3600*int(ora)+60*int(minuto)+int(secondi)

    datenow=datetime.now()
    print("\n")
    print("\nOggi è il {:}/{:}/{:} e sono le {:}:{:}:{:} \n".format(datenow.day,datenow.month,datenow.year,datenow.hour,datenow.minute,datenow.second))
    print('Tu sei nato il:  {:}/{:}/{:}  {:}:{:}:{:}\n'.format(giorno,mese,anno,ora,minuto,secondi))
    print("\nQuindi facendo due calcoli...\n")


    mydate_str= "{:}-{:}-{:} {:}:{:}:{:}".format(giorno,mese,anno,ora,minuto,secondi)
    mydate=datetime.strptime(mydate_str, "%d-%m-%Y %H:%M:%S")
    timediff=datenow-mydate

    anni_fin=round(timediff.days/365)
    print("\nSono passati esattamente: {:} anni, {:} giorni e in totale {:} secondi \n".format(anni_fin,timediff.days,round(86400*timediff.days+timediff.seconds)))



