def pr(arr):
    for i in range(19): 
        for j in range(19): 
            print(arr[i][j], end = " ") 
        print()  

    print("\n\n")

def main():
    #initialize array
    arr = [[0 for i in range(19)] for j in range(19)]

    #take the user input
    n = int(input())

    for i in range(n):
        a, b = input().split()

        a = int(a)
        b = int(b)

        arr[a-1][b-1] = 1

    pr(arr)


main()