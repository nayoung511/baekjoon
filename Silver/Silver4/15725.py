def main():
    c = input()

    if 'x' in c:
        a = c.split('x')

        if a[0] == '-':
            print(-1)
        elif a[0] =='':
            print(1)
        else:
            print(a[0])
    
    else:
        print(0)

main()