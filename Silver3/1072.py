x, y = map(int, input().split())

left = 0
right = x
mini = x

if (x != y):
    z = 100 *y /x

    if z >= 99:
        print(-1)
    else:
        while left <= right:
            mid = (left+right) // 2
            if (100 * (y+mid)) // (x+mid) > z:
                mini = mid
                right = mid - 1
            else:
                left = mid+1

        print(mini)

else:
    print(-1)
"""
(y/x) * 100 = z
(y+k) / (x + k) * 100 = z+1
k = (xz + x - 100 * y) / (99-z)

"""