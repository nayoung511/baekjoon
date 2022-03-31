from sys import stdin

def zero(arr, n, zero_arr):
    if arr == zero_arr:
        count[1] += 1
    else:
        l = n // 3
        if l >= 1: 
            zero_arr = ([row[0:l]] for row in zero_arr[0:l])
            print(zero_arr)
            # 0 - 3 (세로)
            zero([row[0:(l)] for row in arr[0:(l)]], l, zero_arr)
            zero([row[(l):2*l] for row in arr[(0):(l)]], l, zero_arr)
            zero([row[(2*l):n] for row in arr[(0):(l)]], l, zero_arr)

            # 3 - 6 (세로)
            zero([row[(0):l] for row in arr[(l):(2*l)]], l, zero_arr)
            zero([row[(l):2*l] for row in arr[(l):(2*l)]], l, zero_arr)
            zero([row[(2*l):n] for row in arr[(l):(2*l)]], l, zero_arr)

            # 6 - 9
            zero([row[(0):l] for row in arr[(2*l):(n)]], l, zero_arr)
            zero([row[(l):2*l] for row in arr[(2*l):(n)]], l, zero_arr)
            zero([row[(2*l):n] for row in arr[(2*l):(n)]], l, zero_arr)


def one(arr, n, one_arr):
    if arr == one_arr:
        count[2] += 1
    else:
        l = n // 3
        if l >= 1: 
            one_arr = ([row[0:l]] for row in one_arr[0:l])
            # 0 - 3 (세로)
            one([row[0:(l)] for row in arr[0:(l)]], l, one_arr)
            one([row[(l):2*l] for row in arr[(0):(l)]], l, one_arr)
            one([row[(2*l):n] for row in arr[(0):(l)]], l, one_arr)

            # 3 - 6 (세로)
            one([row[(0):l] for row in arr[(l):(2*l)]], l, one_arr)
            one([row[(l):2*l] for row in arr[(l):(2*l)]], l, one_arr)
            one([row[(2*l):n] for row in arr[(l):(2*l)]], l, one_arr)

            # 6 - 9
            one([row[(0):l] for row in arr[(2*l):(n)]], l, one_arr)
            one([row[(l):2*l] for row in arr[(2*l):(n)]], l, one_arr)
            one([row[(2*l):n] for row in arr[(2*l):(n)]], l, one_arr)

def minusOne(arr, n, minusone_arr):
    if arr == minusone_arr:
        count[0] += 1
    else:
        l = n // 3
        if l >= 1: 
            minusone_arr = ([row[0:l]] for row in minusone_arr[0:l])
            # 0 - 3 (세로)
            minusOne([row[0:(l)] for row in arr[0:(l)]], l, minusone_arr)
            minusOne([row[(l):2*l] for row in arr[(0):(l)]], l, minusone_arr)
            minusOne([row[(2*l):n] for row in arr[(0):(l)]], l, minusone_arr)

            # 3 - 6 (세로)
            minusOne([row[(0):l] for row in arr[(l):(2*l)]], l, minusone_arr)
            minusOne([row[(l):2*l] for row in arr[(l):(2*l)]], l, minusone_arr)
            minusOne([row[(2*l):n] for row in arr[(l):(2*l)]], l, minusone_arr)

            # 6 - 9
            minusOne([row[(0):l] for row in arr[(2*l):(n)]], l, minusone_arr)
            minusOne([row[(l):2*l] for row in arr[(2*l):(n)]], l, minusone_arr)
            minusOne([row[(2*l):n] for row in arr[(2*l):(n)]], l, minusone_arr)

n = int(input())
count = [0, 0, 0] #-1, 0, 1
zero_arr = [[0] * (n)] * (n)
one_arr = [[1] * (n)] * (n)
minusone_arr = [[-1] * (n)] *(n)

arr= [list(map(int, stdin.readline().split())) for _ in range(n)]

one(arr, n, one_arr)
zero(arr, n, zero_arr)
minusOne(arr, n, minusone_arr)
for i in count:
    print(i)
