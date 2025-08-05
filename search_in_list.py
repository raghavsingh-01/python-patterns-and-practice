#This program of function that search the entered number from given list

def search_ele(list) :
    print(list)
    m=len(list)
    n=0
    num=int(input("Enter the number :"))
    pos=-1
    
    while n<m :
        sear=list[n]
        if(sear==num):
            pos=n
        n+=1
        
    if(pos>-1) :
        print("Number found at",pos+1,"position")
    else :
        print("Not found !")
    
lis = [2,3,4,78,8,5]
search_ele(lis)