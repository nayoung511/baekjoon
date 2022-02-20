def main():
    while True:
        s = input()

        if s == '0':
            break
            
        if s == s[::-1]:
            print("yes")

        else:
            print("no")
"""
def main():
    str = list()
    while True:
        val = input()
        if val != '0':
            str.append(val)
        elif val == '0':
            #0이 들어올 시 멈춤
            break
    
    #print(str)
    count = 0

    for i in range(len(str)):
        count = 0
        for j in range(int(len(str[i])/2)):
            #print(str[i][j], str[i][len(str[i]) - j - 1])
            if(str[i][j] == str[i][len(str[i]) - j - 1]):
                count += 1
            else:
                print("no")
                j = int(len(str[i])/2)
        
        if count == int(len(str[i])/2):
            print("yes")
"""

main()