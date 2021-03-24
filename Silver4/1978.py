def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def main():
    c = int(input())
    a = list(map(int, input().split()))
    b = []
    a.sort()

    if a[0] == 1:
        a.remove(a[0])
        
    b = prime_list(a[-1] + 1)

    count = 0
    for i in range (len(a)):
        if a[i] in b:
            count +=1

    print(count)
main()