import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
    func = input().rstrip()
    n = int(input())
    num = input()

    #[0,0,0,0]에서 숫자만 추출하기
    num = num[1:-2]
    num = num.split(",")

    #함수 콜 실행
    # R: 뒤집기
    # D: 첫 수 pop
    start = 0
    error = False
    evenR = False

    for i in func:
        if i == 'R':
            if evenR == False: #홀수로 뒤집었다면
                start = len(num) - 1;
                evenR = True
            else: # 짝수로 뒤집었다면
                start = 0
                evenR = False
        if i == 'D':
            if n == 0:
                error = True
                break
            if len(num) > 0:
                num.pop(start)
                if start > 0:
                    start = start - 1
            else:
                error = True
                break
            
    if error == False:
        # check the length
        if len(num) == 0:
            print("[]")
        else:
            if evenR == False:
                print("[",end='')
                for i in range(len(num)-1):
                    print(num[i],end=',')
                print(num[-1],end='')
                print("]")
            else:
                num.reverse()
                print("[",end='')
                for i in range(len(num)-1):
                    print(num[i],end=',')
                print(num[-1],end='')
                print("]")        
    else:
        print("error")

    
