#This the program of function to find the factorial of entered value

def fact_fun(num) :
    n=1
    pro=1
    
    while n<=num :
        pro*=n
        n+=1
    print("Factorial of", num, "is", pro)
    
num = int(input("Enter a number :"))
fact_fun(num)