
# Program : Python Program to Swap two Variables. 



# def swapping(num1, num2):
#     print(f"Before Swapping : num1 = {num1} and num2 = {num2}")
#     temp = num1
#     num1 = num2
#     num2 = temp 
#     print(f"After Swapping : num1 = {num1} and num2 = {num2}")
    



# swapping(2,4)





# num1  = int(input("Enter num1 : "))
# num2  = int(input("Enter num2 :"))

# print(f"Before Swapping : num1 = {num1} and num2 = {num2}")
# num1 = num1 - num2
# num2 = num1 + num2
# num1 = num2 - num1
# print(f"After Swapping : num1 = {num1} and num2 = {num2}")
    




num1  = int(input("Enter num1 : "))
num2  = int(input("Enter num2 :"))

print(f"Before Swapping : num1 = {num1} and num2 = {num2}")

num1 , num2 = num2 , num1

print(f"After Swapping : num1 = {num1} and num2 = {num2}")


