def pisanoPeriod(m):
    a,b = 0, 1
    for i in range(0, m * m):
        a,b = b,(a+b) % m 
        if (a == 0 and b == 1):
            return i + 1







def last_digit(n):
  a,b=0,1
  if (n == 0):
        return 0
  if (n == 1):
        return 1
  else:
      rem = n % pisanoPeriod(10)
      if(rem == 0):
          return 0
      for i in range(1, rem + 2):
          temp =(a+b)% pisanoPeriod(10)
          a = b
          b = temp  
      return(b-1)






if __name__=='__main__':
  m,n = map(int,input().split())
  print((last_digit(n)-last_digit(m-1))%10)

