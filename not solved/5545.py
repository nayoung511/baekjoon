def best_pizza(a, b, c, topping):
    bp = 0
    

# n: 토핑 종류의 수
# a: 도우의 가격, b: 토핑의 가격
# c: 도우의 열량 
n = int(input())
a, b = map(int, input().split())
c = int(input())
topping =[]
for i in range (n):
    topping.append(int(input()))

topping.sort(reversed=True)
bp = 0

# 토핑이 필요한지
bp = a // b


"""
3
12 2
200
50
300
100
---
37

두 번째와 세 번째 토핑을 올리면 200 + 300 + 100 = 600 칼로리가 된다. 
가격은 12 + 2 * 2 = 16원이 된다. 이 피자의 1원 당 칼로리는 600 / 16 = 37.5이다. 
이 피자는 최고의 피자이므로, 37.5의 소수점 이하를 버린 37을 출력하면 된다.
"""