from sys import stdin


def blueCheck(s, num, blue):
    blueP = [[1] * (s)] * (s)
    print_arr(num)
    print()
    print_arr(blueP)

    if num != blueP:
        l = s//2
        blueCheck(l, [row[0:(l)] for row in num[0:(l)]], blue)
        blueCheck(l, [row[(l):s] for row in num[0:(l)]], blue)
        blueCheck(l, [row[0:(l)] for row in num[(l):s]], blue)
        blueCheck(l, [row[(l):s] for row in num[(l):s]], blue)
    else:
        blue += 1
        print("here!", blue)
    return blue

def whiteCheck(s, num, white):
    whiteP = [[0] * (s)] * (s)

    if num != whiteP:
        l = s//2
        whiteCheck(l, [row[0:(l)] for row in num[0:(l)]], white)
    else:
        white+= 1
        b += 1
    
    return white


def print_arr(arr):
    for x in arr:  # outer loop  
        for i in x:  # inner loop  
            print(i, end = " ") # print the elements  
        print()  

def split(s, num, blue, white):
    # n * n 사이즈인지 확인
    whiteP = [[0] * (s)] * (s)

    #print_arr(num)
    #print(blueP, whiteP)

    for i in range (s):
        if num == blueP:
            blue+=1
        if num == whiteP:
            white+=1
    l = s//2
    if l >= 1:
        split(l, [row[0:(l)] for row in num[0:(l)]], blue, white)
        #split(l, [row[0:(l)] for row in num[(l):s]], blue, white)
        #split(l, [row[(l):s] for row in num[0:(l)]], blue, white)
        #split(l, [row[(l):s] for row in num[(l):s]], blue, white)

    return blue, white


def main():
    n = int(input())
    arr= [list(map(int, stdin.readline().split())) for _ in range(n)]
    a1 = [row[0:(n//2)] for row in arr[(n//2):n]]
    #print_arr(a1)
    #print_arr(arr[0:(n//2),0:(n//2)])
    blue = 0
    white = 0

    blueC = blueCheck(n, arr, blue)
    print(blueC)
    print(white)
main()

