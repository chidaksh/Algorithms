def binarysearch(x,ls,start,end):
  if end>=start:
    mid = start + (end-start)//2
    if ls[mid]==x:
      return mid
    elif ls[mid]>x:
      #print(1)
      return binarysearch(x,ls,start,mid-1)
    else :
      #print(0)
      return binarysearch(x,ls,mid+1,end)
  else:
    return -1










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
    a=binarysearch(i,ls,0,n-1)
    while(a>=1):
      if(ls[a]==ls[a-1]):
        a=a-1
      else:
        break
    temp.append(a)
    #print(temp)
  index=0
  for x in temp:
    print(x,end='')
    if(index<len(temp)-1):
      print(" ",end='')
    index+=1
