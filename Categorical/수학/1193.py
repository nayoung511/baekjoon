def main():
    x = int(input())
    numerator = 1
    denominator = 1
    i = 2
    result = 1
    
    #find out which column x belongs
    while(x > result):
        result = result + i
        i = i+1

    #if the i-1 is odd, decreasing e.g)15,14...
    #else, increasing e.g) 4,5,6...

    if((i-1)%2 != 0):
        diff = result - x
        denominator = (i-1) - diff
        numerator = 1 + diff

    else:
        diff = abs(result - x)
        denominator = denominator + diff
        numerator = i - 1 - diff

    print(str(numerator) + '/'+str(denominator))

main()