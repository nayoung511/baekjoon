def bigger_than_ten(n):
    if n >= 10:
        n = n % 10
    return n

def main():
    n = int(input())

    one_digit = n % 10      #1의 자리
    tenth_digit = (int)(n / 10)    #10의 자리 
    #cycle 횟수
    cycle = 0

    while(True):
        cycle += 1
        value = one_digit + tenth_digit

        tenth_digit = bigger_than_ten(one_digit)
        one_digit = bigger_than_ten(value)

        #check if it's same as n
        if(tenth_digit * 10 + one_digit == n):
            break

        #print("cycle ", cycle, tenth_digit, one_digit)

    print(cycle)    

main()