
# Program : Python Program to Convert kilometers to Miles. 


num = float(input("Enter the value of num (in km) :"))

def kilometer_to_miles(num):
    One_miles =  0.62137
    result_miles = num * One_miles
    
    return result_miles



result_miles_user = kilometer_to_miles(num)
print(f"the {num} km is equal to : {result_miles_user} miles")

    
    