def perm(remaining, candidate=''):
 
    if len(remaining) == 0:
        print(candidate)
 
    for i in range(len(remaining)):
 
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
 
        perm(newRemaining, newCandidate)
 
 
if __name__ == '__main__':

    s = input()
    perm(s)