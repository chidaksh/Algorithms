if __name__=='__main__':
  n,w = map(int,input().split())
  ls=[]
  sum=0
  for i in range(n):
    a,b=map(int,input().split())
    ls.append([a,b,a/b])
  ls = sorted(ls,key= lambda x:x[2],reverse=True)
  for i in range(n):
    if ls[i][1]<w:
      sum+=ls[i][0]
      w = w - ls[i][1]
    elif ls[i][1]>w:
      sum+=ls[i][2]*w
      w = 0
      break;
    else:
      sum+=ls[i][0]
      break;
  sum = (sum*10000)/10000
  print(round(sum,4))

