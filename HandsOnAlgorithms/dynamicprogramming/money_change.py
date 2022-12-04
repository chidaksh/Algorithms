if __name__ == "__main__":

    money = int(input())

    ls = [None]*(money+1)
    ls[0] = 0
    for i in range(1,money+1):
        if i>=4:
            ls[i] = min(ls[i-1],ls[i-3],ls[i-4])+1
        elif i>=3:
            ls[i] = min(ls[i-1],ls[i-3])+1
        elif i>=1:
            ls[i] = ls[i-1]+1
        else:
            print("error")
    print(ls[-1])
