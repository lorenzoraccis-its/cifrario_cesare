ROSSO   = "\033[31m" #per colorare le scritte
RESET   = "\033[0m"

def brute_force(testo:str,key:int =0,numeri:list = None) -> list[tuple[int, str]] :
    ris = [] #sta lista contiene le decifrazioni
    for key in range(26) :
        numeri = []
        for idx in range(len(testo)):
            i=testo[idx]
            numeri.append(testo[idx])
            numeri[idx] = ord(numeri[idx])
            if i.isalpha():
                if i.isupper():
                    numeri[idx] -= 65
                    numeri[idx] = (numeri[idx] + key) % 26
                    numeri[idx] += 65
                elif i.islower():
                    numeri[idx] -= 97
                    numeri[idx] = (numeri[idx] + key) % 26
                    numeri[idx] += 97
            numeri[idx] = chr(numeri[idx])
        ris.append((key, "".join(numeri))) #stampa chiave + la tupla con le decifrature oh yes
    return ris #ritorna l'insieme di tutte le cifrature fatte





def main():
    parole = ["di", "che", "e", "il", "la"] #parole comuni nell'italiano
    print("!!Brute forcing del cifrario di cesare!!\n")
    testo = input("Inserire il testo da decifrare : ")
    print (brute_force(testo,key=0,numeri=[]))
    print("\nFINITO!!")





if __name__ == "__main__":
    main()