def lisWithNumber(seq,studseq,n, numToCheck):
    seq = list(map(int, seq))
    studseq = list(map(int, studseq))
    i = 0
    while seq[i] != numToCheck:
        i += 1
    inf = lis_inf(seq[:i], numToCheck)
    sup = lis_sup(seq[i + 1:], numToCheck)
    sub_len=inf+sup+1
    if n==sub_len:
        print("Lunghezza fornita corretta: "+str(n))
    else:
        print("Lunghezza fornita sbagliata\n")
    check=0
    for i in range(0, n-1):
        if studseq[i] == numToCheck:
            check = 1
    if check==0:
        print("Non hai inserito una sequenza contenente il numero: "+str(numToCheck))
        return
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


def lis_inf(seq, numToCheck):
    seq = list(map(int, seq))
    res=[]
    lista = [[] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[i] > seq[j] and len(lista[i]) < len(lista[j]) + 1:
                lista[i] = list(lista[j])
        lista[i].append(seq[i])

    for elem in lista:
        if elem[len(elem)-1] < numToCheck:
            res.append(elem)
    max = 0
    for elem in res:
        if len(elem)>=max:
            max=len(elem)
    return max

def lis_sup(seq, numToCheck):
    seq = list(map(int, seq))
    res = []
    lista = [[] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[i] > seq[j] and len(lista[i]) < len(lista[j]) + 1:
                lista[i] = list(lista[j])
        lista[i].append(seq[i])

    for elem in lista:
        if elem[0] > numToCheck:
            res.append(elem)
    max = 0
    for elem in res:
        if len(elem) >= max:
            max = len(elem)
    return max

# if __name__ == "__main__":
#     seq=[34,42,44,49,41,52,63,69,40,60,86,45,66,54,79,81,43,46,38,61,80,48,64,73,47]
#     studseq=[34, 41, 45, 54, 61, 64, 73]
#     n=7
#     #print("Sequenza iniziale:\n"+str(seq))
#     #print("Fist algo:\n")
#     #longest_increasing_subsequence(seq,studseq,n)
#     #print("\nSecond algo:\n")
#
#
#     lisWithNumber(seq,studseq,n, 40)

