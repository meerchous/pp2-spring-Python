def histogram(list):
    for i in range(len(list)):
        for j in range(list[i]):
            print("*", end="")
histogram(input().split())
