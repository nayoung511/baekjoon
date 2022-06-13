"""
상근 승리
1, 3, 4, 5개가 남았을 때

창영 승리

"""

n = int(input())
total = [0, True,False,True,True] + [0]*(n-4)
 
for _ in range(5,n+1):
    if False in [total[_-1],total[_-3],total[_-4]]:
        total[_]= True
    else:
        total[_]=False
 
if total[n]:
    print("SK")
else:
    print("CY")