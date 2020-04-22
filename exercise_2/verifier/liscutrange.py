def lis(seq,studseq,n):
    seq = list(map(int, seq))
    studseq = list(map(int, studseq))
    lista = [[] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in range(0,i):
            if seq[i] > seq[j] and len(lista[i]) < len(lista[j])+1:
                lista[i] = list(lista[j])
        lista[i].append(seq[i])
    max=0
    for elem in lista:
        if max<len(elem):
            max=len(elem)

    if n==max:
        print("Lunghezza fornita corretta: "+str(n))
    else:
        print("Lunghezza fornita sbagliata\n")
    for i in range(1,n):
        if studseq[i-1]>studseq[i]:
            print("Non hai inserito una sequenza crescente")
            return
    i=0
    j=0
    while i!=n and j!=len(seq):
        if studseq[i]==seq[j]:
            i+=1
            j+=1
        else:
            j+=1
    if i==n:
        print("Sottosequenza fornita corretta: " + str(studseq))
    else:
        print("Sottosequenza fornita sbagliata\n")

def lisSubwithoutElementInRange(seq,studseq,n,start,stop):
    aux=seq[:]
    del aux[start:stop]
    lis(aux,studseq,n)

# if __name__ == "__main__":
#     seq=[34,42,44,49,41,52,63,69,40,60,86,45,66,54,79,81,43,46,38,61,80,48,64,73,47]
#     studseq=[34, 42, 44, 49, 52, 60, 61, 64, 73]
#     n=9
#     #print("Sequenza iniziale:\n"+str(seq))
#     #print("Fist algo:\n")
#     #longest_increasing_subsequence(seq,studseq,n)
#     #print("\nSecond algo:\n")
#     lisSubwithoutElementInRange(seq,studseq,n,12,16)