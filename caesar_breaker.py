


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
        i=testo[idx]
    return numeri




def main():
    print("!!Brute forcing del cifrario di cesare!!\n")
    testo = input("Inserire il testo da decifrare : ")
    n=0
    while n <26 :
        numeri = []
        print("".join(brute_force(testo,n,numeri)))
        print("---------------------------------------------")
        n+=1
    print("\nFINITO!!")




if __name__ == "__main__":
    main()