def calculate(a, l, h, sum):
    result = sum
    
    for i in range(1, h+1):
        print("\n-----------------\n", i)
        print(a[l], a[h], sum)
        print(a[l:h+1])

        if (a[l] > sum and a[h] > sum) or (a[l] < sum and a[h] < sum):
            sum = sum / a[l]
            sum = sum / a[h]
            return calculate(a, l+1,h-1, sum)


        else:
            if a[l] < a[h]:
                print("here")
                if a[l] != 0.0:
                    sum = sum / a[l]
                if result < sum:
                    result = sum
                l = l + 1
            else:
                print("hi")
                if a[h] != 0.0:
                    sum = sum / a[h]
                if result < sum:
                    result = sum
                h = h - 1

    return result



def main():
    c = int(input())
    a = []
    sum = 1

    for i in range (c):
        k = float(input())
        sum = sum * k
        a.append(k)
        

    l = 0
    h = c - 1

    t = calculate(a, l, h,sum)
    print(t)
    
"""
    for i in range (1, c):
        left = a[l]
        right = a[h]
        #1. list의 양 끝을 sum과 비교한다
        #왼쪽 끝과 오른쪽 끝 중 어느 것이 더 큰 지 비교 (작은 걸 제외시켜야 한다)
        #print("\n----------------------------",i)
        #print("left:",left, "right", right)


        if left > right: #오른쪽을 제외한다
            #print(right, "is smaller than", left)
            if right > sum:
                #두 수 다 sum보다 크다면, 다음 수를 비교한다
                if a[c-i] > a[i]:
                    sum = sum / left
                    if result < sum:
                        result = sum
                    l = l+1

            else:
                if right != 0.0:
                    sum = sum / right
                    if result < sum:
                            result = sum
                    h = h-1
                else:
                    h = h-1

            #print(sum, left, right)
            #print(a[l:h+1])


        else: #왼쪽을 제외한다
            #print(right, "is bigger than", left)
            if left > sum:
                #print("but", left, "is bigger than sum", sum)
                #print("comparing next values", a[i], "and", a[c-i])
                if a[i] > a[c-i]:
                    sum = sum / right
                    if result < sum:
                        result = sum
                    h = h-1

            else:
                if left != 0.0:
                    sum = sum / left
                    if result < sum:
                            result = sum
                    l = l+1
                else:
                    l = l+1

            #print(round(sum,4), left, right)
            #print(a[l:h+1])

    print(result)
"""
main()