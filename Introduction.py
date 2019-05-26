##Introduction
#---------------------------------------Say "Hello, World!" With Python-----------------------------------------------------

print("Hello, World!")

#------------------------------------------------Python If-Else-------------------------------------------------------------


num = int(input()) 
n = num % 2 

if n == 0 and (2<= num <=5): 
    print('Not Weird')
elif n == 0 and (6<= num <=20): 
    print('Weird')
elif n == 0 and num > 20: 
    print("Not Weird")
elif num % 2 != 0: 
    print('Weird')


#------------------------------------------------Arithmetic Operators-----------------------------------------------------------

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("%d \n%d \n%d" %(a+b, a-b, a*b))
    

#--------------------------------------------------------Loops-------------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())

    for i in range(0,n):
        print("%d" %(i*i))

#-----------------------------------------------------Write a function------------------------------------------------------------



def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%100 ==0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:

            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))


#-------------------------------------------------------------print function------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep='')


