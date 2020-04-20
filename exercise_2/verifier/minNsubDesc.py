def minimoNumSottosequenzeDecConTuttiGliElementi(seq,studseq,n):
    seq = list(map(int, seq))
    studseqint=[]
    for elem in studseq:
        aux = []
        for num in elem:
            if num!='':
                aux.append(int(num))
        studseqint.append(aux)

    print(str(studseqint))
    res = []
    aux = [seq[0]]
    for i in range(len(seq)-1):
        if seq[i] > seq[i + 1]:
            aux.append(seq[i + 1])
        else:
            res.append(aux)
            aux = [seq[i + 1]]
    res.append(aux)
    print(str(res))
    if len(res)==n:
        print("Numero di sottosequenze descrescenti corrette\n")
    else:
        print("Numero di sottosequenze descrescenti errato\n")




if __name__ == "__main__":
    seq=['34','42','44','49','41','52','63','69','40','60','86','45','66','54','79','81','43','46','38','61','80','48','64','73','47']
    studseq=[['34','','',''],['42','41','40','38'],['44','43','',''],['49','45','',''], ['52','46','',''], ['63','60','54','48'], ['69','66','61',''], ['86','79','64','47'], ['81','80','73','']]

    n=9
    #print("Sequenza iniziale:\n"+str(seq))
    #print("Fist algo:\n")
    #longest_increasing_subsequence(seq,studseq,n)
    #print("\nSecond algo:\n")
    minimoNumSottosequenzeDecConTuttiGliElementi(seq,studseq,n)