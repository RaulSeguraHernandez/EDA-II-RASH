def merge(A):
    #verificar caso base
    if len(A) >1:
        mid = len(A)//2
        L= A[:mid]
        R= A[mid:]
        merge(L)
        merge(R)
        i,j,k=0
        while (i<len(L) and j<len(R)):
            if L[i]<=R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            A[k]= L[i]
            k+=1
            i+=1
        while j<len(R)
            A[k]= R[j]
            k+=1
            j+=1
