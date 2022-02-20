s = input()

def checkPalin(s):
    if s[::-1] == s:
        return True
# if it is already a palindrome
if checkPalin(s):
    print(len(s))

else:
    for i in range (len(s)):
        # a[::-1] = all items in the array, reversed
        # 앞에서 하나씩 늘려가면서 스트링에 append해준다
        temp = s + s[:i][::-1]
        if checkPalin(temp):
            #print("True!")
            s=temp
            print(len(s))
            break

#print(s)
    