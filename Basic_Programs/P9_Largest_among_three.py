
# Program : Python Programs to find the Largest among three number. 


num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
num3 = int(input("Enter the value of num3 :"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is largest number than {num2} and {num3}")
    
    
elif num2 > num3 and num2 > num1:
    print(f"{num2} is largest number than {num1} and {num3}")
    
    
elif num3 > num2 and num3 > num1:
     print(f"{num3} is largest number than {num1} and {num2}")
    
    
    
    
    