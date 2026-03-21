
# Program : Python Program to Check Leap Year. 

# Leap_year : year%400 == 0 or ((year%4 == 0) and (year%100 != 0))


year = int(input("Enter the year :"))

def leap_year(year):
    if year%400 == 0 or ((year%4 == 0) and (year%100 != 0)):
        print(f"{year} is a leap year")
        
    else:
        print(f"{year} is not a leap year")
    
    
leap_year(year)