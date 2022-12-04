def febonaccimod(n):
  pisano_period = 60
  n = n % pisano_period
  a,b = 0, 1
  if n==0:
        return 0
  elif n==1:
        return 1
  for i in range(n-1):
      a,b = b, a+b
  return (b% 10)   








if __name__=='__main__':
    n = int(input())
    print((febonaccimod(n)*febonaccimod(n+1))%10)
