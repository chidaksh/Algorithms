def gcd(a,b):
  if a==0: return b
  if b==0: return a
  return gcd(b,a%b)

def lcm(a,b):
  return int((a/gcd(a,b))*b)



if __name__=='__main__':
  a,b = map(int,input().split())
  print(lcm(a,b))
  
