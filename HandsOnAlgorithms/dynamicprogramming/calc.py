def new_calculator(n):
    for i in range(2,n+1):
        if (i%2 == 0 and i%3 == 0):
            ls[i] = min(ls[(i//3)],ls[(i//2)],ls[(i-1)])+1
        elif (i%2 == 0):
            ls[i] =  min(ls[(i//2)],ls[(i-1)])+1
        elif (i%3 == 0):
            ls[i] =  min(ls[(i//3)],ls[(i-1)])+1
        else:
            ls[i] = ls[(i-1)]+1


def backtrack(n):
    temp = []
    while n != 1:
        temp.append(n)
        if (n%2 == 0 and n%3 == 0):
            if min(ls[(n//3)],ls[(n//2)],ls[n-1]) == ls[(n//3)]:
                n = n//3
            elif min(ls[(n//3)],ls[(n//2)],ls[n-1]) == ls[(n//2)]:
                n = n//2
            else:
                n = n-1
        
        elif (n%2 == 0):
            if min(ls[(n//2)],ls[n-1]) == ls[(n//2)]:
                n = n//2
            else:
                n = n-1

        elif (n%3 == 0):
            if min(ls[(n//3)],ls[n-1]) == ls[(n//3)]:
                n = n//3
            else:
                n = n-1

        else:
            n = n-1
    temp.append(n)
    return temp


if __name__ == "__main__":

    n = int(input())
    global ls
    ls = [None]*(n+1)
    ls[0] = 0
    ls[1] = 0
    new_calculator(n)
    print(ls[-1])
    new_ls = backtrack(n)
    # print(new_ls[::-1])
    for i in new_ls[::-1][:-1]:
        print(i,end = ' ')
    print(new_ls[::-1][-1])
