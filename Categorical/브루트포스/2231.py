def main():
    n = int(input())
    result = 0

    for i in range(1, n+1):
        A = list(map(int, str(i)))
        result = i + sum(A)
        if(result == n):
            print(i)
            break

        #생성자가 없을 경우 0 출력
        if i == n:
            print(0)

    
main() 