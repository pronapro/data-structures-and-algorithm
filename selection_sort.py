def selection(A):
    i =0
    n = len(A)
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if A[j] < A[small]:
                small =j
        if i != small:
            A[i],A[small] = A[small],A[i]
    print(A)
an = [2,7,8,5,3,1,0]
selection(an)
