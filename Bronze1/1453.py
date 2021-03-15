def main():
    noCustomer = int(input())

    checkSeat = [False] * 101
    noSeat = 0
    wantedSeat = list(map(int, input().split()))

    for i in range(noCustomer):
        check = wantedSeat[i]

        if checkSeat[check-1] == False:
            checkSeat[check-1] = True

        elif checkSeat[check-1] == True:
            noSeat+=1

    print(noSeat)

main()