def sumA(listA,S):
    n = len(listA)
    for i in range(1,n):
        if int(listA[i-1])+int(listA[i]) ==S:
            print("its {} and {}".format(listA[i-1],listA[i]))
lsA = [3,2,1,4,6,4,7,10,2]
S =12
sumA(lsA,S)
