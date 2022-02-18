def histogram(list):
    for i in range(len(list)):
        for j in range(int(list[i])):
            if j == int(list[i])- 1:
                print("*")
            else:
                print("*", end = "")
n = input().split()
histogram(n)
