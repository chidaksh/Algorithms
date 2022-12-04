def febonacci_fast(n):
  a=1
  b=1
  if n==0: return 0
  if n==1 or n==2: return 1
  for i in range(2,n):
    temp=a+b
    a=b
    b=temp
  return temp



if __name__=='__main__':
  print(febonacci_fast(int(input())))
