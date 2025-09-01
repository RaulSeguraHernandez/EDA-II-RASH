def swap(A,x,y):
  temp = A[x]
  A[x]=A[y]
  A[y]= temp

def partition(A,p,r):
  x=A[r]
  i = p-1
  for j in range(p,r):
    if(A[j]<=x):
      i+=i
      swap(A,i,j)
  swap(A,i+1,r)
  return i+1
def Quick(A,p,r):
  if(p<r):
      q= partition(A,p,r)
  Quick(A,p,q-1)
  Quick(A,q+1,r)


      
