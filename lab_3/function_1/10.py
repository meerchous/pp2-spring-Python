def sph_vol(list):
    for i in range(len(list)):
        s = 0
        for j in range(len(list)):
            if list[i] == list[j]:
                s += 1
        if s == 1:
            print(list[i])
sph_vol(input().split())