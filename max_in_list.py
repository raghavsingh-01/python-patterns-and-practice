#This the program of the function that find out the maximum no. from the list

def max_list(list) :
    print(list)
    n=len(list)
    max,m = 0,0
    while m<n :
        if list[m]>max :
            max = list[m]
        m+=1
    print("Maximum number in the given list is",max)
     
list=[1,2,3,4,6,65,64,23,9]
max_list(list)