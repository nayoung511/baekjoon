import math

def main():
    # A = climbing
    # B = sliding
    # V = height of tree

    a, b, v = input().split()

    a = int(a)
    b = int(b)
    v = int(v)

    # check if the climbing == height
    n = (v-b)/(a-b)

    print(math.ceil(n))
main()