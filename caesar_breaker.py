ROSSO   = "\033[31m" #per colorare le scritte
RESET   = "\033[0m"

def brute_force(testo:str,key:int,numeri:list) -> list[tuple[int, str]] :

    for idx in range(len(testo)):
        i=testo[idx]
        numeri.append(testo[idx])
        numeri[idx] = ord(numeri[idx])
        if i.isalpha():
            if i.isupper():
                numeri[idx] -= 65
                numeri[idx] = (numeri[idx] - key) % 26
                numeri[idx] += 65
            elif i.islower():
                numeri[idx] -= 97
                numeri[idx] = (numeri[idx] - key) % 26
                numeri[idx] += 97
        numeri[idx] = chr(numeri[idx])
    return numeri




def main():
    parole = ["di", "che", "e", "il", "la"] #parole comuni nell'italiano
    print("!!Brute forcing del cifrario di cesare!!\n")
    testo = input("Inserire il testo da decifrare : ")
    n=0
    while n <26 :
        numeri = []
        print (f"chiave {n}") #cosi capiamo quale chiave è stata usata per ciascuna decifratura
        decifrato ="".join(brute_force(testo,n,numeri)) #mettiamo la decifratura in una variabile
        individua_parole = decifrato.split() #separiamo i caratteri facendoli diventare parole
        if any(parola in individua_parole for parola in parole): #controlla ogni parola nella frase e vede se c'è almeno un elemento della lista nella frase
                print(f"{ROSSO}{decifrato}{RESET}") #printa in rosso
        else:
            print(f"{decifrato}")
        print("---------------------------------------------")
        n+=1
    print("\nFINITO!!")





if __name__ == "__main__":
    main()