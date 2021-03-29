"""
입력 정답 출력
321   9  10
609  10  11
642  10  11
643  11  12
645  11  12
963  10  11
"""

def main():
    c = int(input())
    count = 0
    dp = [[2e9]*3]*(c+1)
    dp[1][0] = dp[1][1] = dp[1][2] = 0

    for i in range (2, c+1):
        if i % 3 == 0:
            
main()