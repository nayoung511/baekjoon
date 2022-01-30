n = int(input())
a = [0] * (n+1)
def dp(n):
    if n <= 3: return 1
    if n == 4: return 2
    if n == 9: return 3
    
        
    
    n = n - dp(n) 
    
        
