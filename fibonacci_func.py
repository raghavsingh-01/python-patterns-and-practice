#This is the code of the function that print the fibonacci series till that entered number

def fibo_func(num) :
    n1 = 1
    n2 = 0
    sum = 0
    temp = None
    
    while sum  <= num :
        print(sum , end=" ")
        temp = n1
        n1 = sum
        n2 = temp
        sum = n1 + n2 
        
num=int(input("Enter the number till where you want Fibonacci Series :"))
fibo_func(num)   