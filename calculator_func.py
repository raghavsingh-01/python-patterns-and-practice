#This is the program of function that works with with some arithmetic function

def calculate_func(n1,n2) :
    print("Enter 1.Multiplication 2.Addition 3.Substraction 4.Division")
    op = int(input())
    
    if op==1 :
        cal = (n1*n2)
    elif op==2 :
        cal = (n1+n2)
    elif op==3 :
         cal = (n1-n2)
    elif op==4 :
         cal = (n1/n2)
    else :
         print("Enter the given numbers only!")
         exit()
     
    print("The result is",cal)
     
print("Enter two numbers :-")
n1 = int(input("Number 1 :"))
n2 = int(input("Number 2 :"))
calculate_func(n1,n2)