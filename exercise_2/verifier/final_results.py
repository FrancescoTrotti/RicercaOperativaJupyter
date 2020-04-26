def save_results():
    file1 = open('../result/es1.txt', 'r')
    p=file1.readlines()

    for i in range(0, len(p)):
        p[i] = list(map(int,p[i]))
    print(str(p))




if __name__ == '__main__':
    save_results()