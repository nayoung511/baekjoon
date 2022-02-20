def main():
    n = int(input())

    i = 1
    result = 1
    while(n > result):
        result = result + i * 6
        i = i+1

    print(i)

main()
