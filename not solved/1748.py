n = int(input())
length = len(str(n))

dig = 0

if n >= 10:
    

    for i in range (length, 0, -1):
        val = pow(10, length-1)
        n = n - val
        dig += n * length + length


print(dig)
