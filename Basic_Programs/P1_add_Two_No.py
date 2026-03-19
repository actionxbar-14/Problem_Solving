
# Program : adding the two number and getting the sum as a result. 

num1 = float(input("Enter the Value of num1 :"))
num2 = float(input("Enter the Value of num2 :"))

def add_two_num(num1,num2):
     
    result_sum = num1 + num2  
    return result_sum



answer_result = add_two_num(num1,num2)

print(f"The sum of {num1} and {num2} is : {answer_result}")