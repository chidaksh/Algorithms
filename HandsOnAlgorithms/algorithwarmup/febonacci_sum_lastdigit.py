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
      for i in range(2, rem + 3):
          temp =(a+b)% pisanoPeriod(10)
          a = b
          b = temp  
      return(b-1)




if __name__=='__main__':
  n = int(input())
  print(last_digit(n)%10)

