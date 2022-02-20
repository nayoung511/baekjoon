def main():
    # A의 수를 재배열 
    # B의 수는 재배열 x 
    i = int(input())

    #가장 큰 수와 가장 작은 수 매칭
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    e = b.copy()
    e.sort(reverse=True)
    sum = 0

    for j in range(i):
        sum = sum + (e[j] * a[j])
    print(sum)

main()