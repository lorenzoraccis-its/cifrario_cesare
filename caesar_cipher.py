
def encrypt(text: str, key: int, numeri: list = None) -> str:
    if numeri is None:
        numeri = []
    for car in text:
        numeri.append(ord(car))
        cifra(key, numeri, len(numeri) - 1)  # passa l'indice dell'ultimo elemento
                 #ed essendo che viene ripetuto in un for, decrementa sempre di uno


    return "".join(chr(c) for c in numeri) #cosi fa un buon output sulla stessa riga (rispettando gli spazi)


def cifra(key: int, numeri: list, idx: int):  # idx è l'indice di aumento
    c = chr(numeri[idx])  #in questa funzione c'è il cambio di valore della lettera (in ASCII)
    if c.isalpha():
        if c.isupper():
            numeri[idx] -= 65
            numeri[idx] = (numeri[idx] + key) % 26
            numeri[idx] += 65
        elif c.islower():
            numeri[idx] -= 97
            numeri[idx] = (numeri[idx] + key) % 26
            numeri[idx] += 97


def main():

    print("Benvenuto nel cifrario di Cesare!")
    scelta=" " #cosi entra nel while
    while scelta != "" : #se si preme INVIO si esce dal loop
        print("""\n\n
              1.cifrare\n
              2.decifrare\n
              Premi INVIO per uscire\n\n
                            """)
        scelta = int(input("Inserisci il numero di scelta: "))
        text = input("\n\nInserisci testo : ")
        key = int(input("Inserisci la chiave : "))
        if scelta == 1:
            print(encrypt(text, key))
        elif scelta == 2:
            print(encrypt(text, -key))
        else:
            print("Arrivederci")

if __name__ == "__main__":
    main()