import sys
input = sys.stdin.readline

def binarySearch(start, end, wifi, maxx):
    while end >= start:
        mid = (end + start) // 2

        if 












# 집의 개수, 공유기의 개수
n, c = map(int, input().split())
wifi = []
for i in range (n):
    wifi.append(int(input()))

binarySearch(0, n-1, wifi, 0)

