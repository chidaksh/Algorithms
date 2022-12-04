if __name__=='__main__':
  d = int(input())
  m = int(input())
  n = int(input())
  ls=[]
  num_refills=0
  ls.append(0)
  temp = input().split()
  for x in temp:ls.append(int(x))
  ls.append(d)
  #print(ls)
  j=0
  #temp=0
  a=0
  while j<=n:
    temp = j
    while (j<=n and ls[j+1]-ls[temp]<=m):
      j+=1
    if j==temp:
      a=1
      break
    if j<=n:
      num_refills+=1
  if a==1:print("-1")
  else: print(num_refills)
