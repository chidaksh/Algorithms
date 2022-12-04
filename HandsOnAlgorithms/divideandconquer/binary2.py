def bsearch(a,n):
    i,j = 0,len(a)
    # k < i => a[k] < n
    # k >= j => a[k] >= n
    while i != j:
        k = i + (j-i)//2
        if a[k] < n: i = k+1
        else: j = k
    return i
 
def find(a,n):
    k = bsearch(a,n)
    if k < len(a) and a[k] == n: return k
    else: return -1

# [(0, 0, None), (1, 0, 0), (2, 1, 1), (3, 3, None), (4, 3, 3), (5, 7, None)]
if __name__=='__main__':
  n= int(input())
  ls = list(map(int,input().split()))
  #n = data1[0]
  #ls = data1[1:]
  ls = sorted(ls)
  #print(ls)
  temp=[]
  k=int(input())
  ls2 = list(map(int,input().split()))
  #k = ls2[0]
  #print(data2[1:])
  for i in ls2:
    a=find(ls,i)
    temp.append(a)
    #print(temp)
  index=0
  for x in temp:
    print(x,end='')
    if(index<len(temp)-1):
      print(" ",end='')
    index+=1
