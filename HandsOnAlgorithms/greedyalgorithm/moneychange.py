def getchange(n):
  m=0
  m+=n//10
  n=n%10
  m+=n//5
  n=n%5
  m+=n//1
  return m







if __name__== "__main__":

  n = int(input())
  print(getchange(n))
