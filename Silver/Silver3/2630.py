from sys import stdin


def blueCheck(s, num, blues):
    blueP = [[1] * (s)] * (s)
    if num != blueP:
        l = s//2
        if l >= 1:
            blueCheck(l, [row[0:(l)] for row in num[0:(l)]], blues)
            blueCheck(l, [row[(l):s] for row in num[0:(l)]], blues)
            blueCheck(l, [row[0:(l)] for row in num[(l):s]], blues)
            blueCheck(l, [row[(l):s] for row in num[(l):s]], blues)
    else:
        blues[0] += 1
        #print("here!", blues)
    return blues

def whiteCheck(s, num, whites):
    whiteP = [[0] * (s)] * (s)

    if num != whiteP:
        l = s//2
        if l >= 1:
            whiteCheck(l, [row[0:(l)] for row in num[0:(l)]], whites)
            whiteCheck(l, [row[(l):s] for row in num[0:(l)]], whites)
            whiteCheck(l, [row[0:(l)] for row in num[(l):s]], whites)
            whiteCheck(l, [row[(l):s] for row in num[(l):s]], whites)
    else:
        whites[0] += 1
        #print("here!", whites)
    return whites

def print_arr(arr):
    for x in arr:  # outer loop  
        for i in x:  # inner loop  
            print(i, end = " ") # print the elements  
        print()  


def main():
    n = int(input())
    arr= [list(map(int, stdin.readline().split())) for _ in range(n)]

    whites = [0]
    blues=[0]

    blueC = blueCheck(n, arr, blues)
    whiteC = whiteCheck(n, arr, whites)
    
    print(*whiteC)
    print(*blueC)
main()

