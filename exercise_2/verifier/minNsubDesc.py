def minimoNumSubDESC(seq,studseq,n):
    seq = list(map(int, seq))
    studseqint=[]
    for elem in studseq:
        aux = []
        for num in elem:
            if num!='':
                aux.append(int(num))
        studseqint.append(aux)

    res=[]
    check=[0 for i in range(len(seq))]
    i=0
    while i!= len(seq)-1:
        if check[i]!=1:
            aux = [seq[i]]
            check[i]=1
            j=i+1
            val=seq[i]
            while j!=len(seq):
                if check[j]!=1:
                    if val>seq[j]:
                        aux.append(seq[j])
                        check[j]=1
                        val=seq[j]
                j += 1
            res.append(aux)
        i+=1

    if len(res)==n:
        print("Numero di sottosequenze descrescenti corrette\n")
    else:
        print("Numero di sottosequenze descrescenti errato\n")

    if res==studseqint:
        print("Soluzione corretta: " + str(studseqint))
    else:
        print("Soluzione sbagliata\n")




# if __name__ == "__main__":
#     seq=['34','42','44','49','41','52','63','69','40','60','86','45','66','54','79','81','43','46','38','61','80','48','64','73','47']
#     studseq=[['34','','',''],['42','41','40','38'],['44','43','',''],['49','45','',''], ['52','46','',''], ['63','60','54','48','47'], ['69','66','61',''], ['86','79','64',''], ['81','80','73','']]
#
#     n=9
#     #print("Sequenza iniziale:\n"+str(seq))
#     #print("Fist algo:\n")
#     #longest_increasing_subsequence(seq,studseq,n)
#     #print("\nSecond algo:\n")
#     minimoNumSottosequenzeDecConTuttiGliElementi(seq,studseq,n)