def longest_increasing_subsequence(seq,studseq,n):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(seq)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < seq[i]] or [[]], key=len)
                 + [seq[i]])
    res=max(l, key=len)
    if n==len(res):
        print("Lunghezza corretta\n")
    else:
        print("Lunghezza sbagliata\n")
    if res==studseq:
        print("Sottosequenza corretta\n")
    else:
        print("Sottosequenza sbagliata\n")