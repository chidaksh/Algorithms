def febonacci_lastdigit(n):
  a=1
  b=1
  if n==0: return a
  if n==1 or n==2: return b
  for n in range(2,n):
    temp = (a+b)% 10
    a=b%10
    b = temp % 10
  return temp%10



if __name__=='__main__':
  print(febonacci_lastdigit(int(input())))
