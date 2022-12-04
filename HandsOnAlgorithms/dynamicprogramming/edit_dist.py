def edit_distance(m,n,i,j):
    if i == 0 and j == 0:
        return 0
    elif i == 0:
        return j+1
    elif j == 0:
        return i+1
    else:
        if m[i] == n[j]:
            return edit_distance(m,n,i-1,j-1)
        else:
            return min(edit_distance(m,n,i,j-1),edit_distance(m,n,i-1,j),edit_distance(m,n,i-1,j-1))+1


    
if __name__ == "__main__":
    m = input()
    n = input()
    dist = edit_distance(m,n,len(m)-1,len(n)-1)
    print(dist)
