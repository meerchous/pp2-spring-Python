def spy_game(x):
    for i in range(len(x)):
        a = False
        if int(x[i]) == 0:
            for j in range(i+1,len(x)):
                if int(x[j]) == 0:
                    for m in range(j+1,len(x)):
                        if int(x[m]) == 7:
                            a = True
                            break
                if a:
                    break               
        if a:
            break
    print(a)

n = input().split()
spy_game(n)