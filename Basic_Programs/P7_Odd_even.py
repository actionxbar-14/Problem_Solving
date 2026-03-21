
# Program : Python Program to Check if a Number is Odd or Even. 


num = int(input("Enter the value of num :"))

def odd_even(num):
    if num > 0 :
        if num % 2 == 0:
            print(f"{num} is an Positive even integer")
            
        else:
            print(f"{num} is an Positive odd integer")
            
    elif num == 0:
        print(f"{num} is not an odd nor an even number")
        
    
    else:
        if num % 2 == 0:
            print(f"{num} is an Negative even integer")
            
        else:
             print(f"{num} is an Negative odd integer")
             
             
             
             
             
odd_even(num)
            
            
     
            
        
    