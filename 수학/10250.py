from array import *

def test(H, W, N):
    #create 2D array
    arr = [[0]*W for i in range(H)]

    row = 1
    col = 1

    for i in range(W):
        for j in range(H):
            if(N > 0):
                arr[j][i] = N
                N = N - 1
                if(N == 1):
                    row = i + 1
                    col = H - j
            else:
                break
                
    #print(col*100 + row)
    return col*100 + row


"""
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
"""

def main():
    T = int(input())    #Test case

    lst = [0]*T

    for i in range(T):
        H, W, N = input().split()

        H = int(H)
        W = int(W)
        N = int(N)

        lst[i] = test(H, W, N)

    for i in range(T):
        print(lst[i])


main()