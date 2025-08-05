#This the program of function that calculate no. of even and odd no. from tje list

def count_even_odd(list):
    print(list)
    n = len(list)
    m = 0
    e = 0
    o = 0
    
    while m < n:
        num = list[m]
        if num % 2 == 0:
            e += 1
        else:
            o += 1
        m += 1
         
    print("Even numbers:", e)
    print("Odd numbers:", o)
    
list=[1,2,3,4,6,65,64,23,9]
count_even_odd(list)