l, r = map(str, input().split())
count = 0
# 8이 있는지 확인

if len(l) != len(r):
    print(0)

else:
    if l[0] != r[0]:
        print(0)
    else:
        if l[0] == '8':
            count+=1
        for i in range (1, len(l)):
            if l[i] != r[i]:
                break
            else:
                if l[i] == '8':
                    count+=1

        print(count)
