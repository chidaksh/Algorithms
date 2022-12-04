if __name__ == '__main__':

  n = int(input())
  ls1=[int(x) for x in input().split()]
  ls2=[int(x)for x in input().split()]
  ls1 = sorted(ls1,reverse=True)
  ls2 = sorted(ls2,reverse=True)

  #print(ls1,ls2)
  sum=0

  for i in range(n):
    sum+=ls1[i]*ls2[i]
  print(sum)
