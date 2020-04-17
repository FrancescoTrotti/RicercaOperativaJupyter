def longest_increasing_subsequence(seq,studseq,n):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(seq)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < seq[i]] or [[]], key=len)
                 + [seq[i]])
    res=max(l, key=len)
    res = list(map(int, res))
    studseq = list(map(int, studseq))
    #print("Sottostringa passata: "+str(studseq)+"\nSottostringa calcolata: "+str(res)+"\nLunghezza passata: "+str(n)+"\nLunghezza calcolata: "+str(len(res)))
    if n==len(res):
        print("Lunghezza fornita corretta: "+str(n))
    else:
        print("Lunghezza fornita sbagliata\n")
    if res==studseq:
        print("Sottosequenza fornita corretta: "+str(studseq))
    else:
        print("Sottosequenza fornita sbagliata\n")