
# Program :  Python Program to check if a Number is Positive , Negative or 0. 

num = int(input("Enter the value on num :"))

def number_Checking(num):
    if num > 0 :
        print(f"{num} is an positive integer")
        
    elif num == 0:
        print(f"{num} is zero")
        
    else:
        print(f"{num} is negative integer")
        
        

number_Checking(num)