def pr(arr):
    for i in range(10): 
        for j in range(10): 
            print(arr[i][j], end = " ") 
        print()  

    print("\n\n")

def main():
    #input the array
    arr = []
    for i in range(10):
        arr.append([int(y)for y in input().split()])

    #i checks for row
    #j checks for column
    j = 1
    i = 1

    while(True):
        #start = [1][1]
        if(arr[1][1] == 2):
            arr[1][1] = 9
            break
        else:
            arr[1][1] = 9
        #always to the right
        #j checks for column

        if(arr[i][j+1] == 0):
            #mark the current pos as 9
            j = j+1
            arr[i][j] = 9

            pr(arr)
            
        #go down
        elif(arr[i][j+1] == 1):
            if(arr[i+1][j] == 1):
                #cannot move anymore
                break

            elif(arr[i+1][j] == 2):
                arr[i+1][j] = 9
                break
                
            else:
                i = i+1
                arr[i][j] = 9

            pr(arr)
           
        elif(arr[i][j+1] == 2):
            if(arr[i][j+1] == 2):
                arr[i][j+1] = 9
                break
            

    # For printing the matrix 
    for i in range(10): 
        for j in range(10): 
            print(arr[i][j], end = " ") 
        print() 


main()