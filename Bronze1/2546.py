def answer():
    count = 0
    n = input()
    if n == '':
        c, e = input().split()
        c = int(c)
        e = int(e)

        cIQ = list(map(int, input().split()))
        eIQ = list(map(int, input().split()))

        cIQavg = sum(cIQ)/c
        eIQavg = sum(eIQ)/e

        # eIQavg < answer <cIQavg

        for i in range (len(cIQ)):
            if cIQ[i] < cIQavg and cIQ[i] > eIQavg:
                count += 1

        print(count)
def main():
    testCase = int(input())

    for i in range(testCase):
        answer()

main()
