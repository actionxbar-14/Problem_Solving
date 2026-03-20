
# Program : Python Program to Calculate the Area of Triangle

def area_of_triangle():
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    area = (1/2)*base*height
    
    return area 


result_area = area_of_triangle()
print(f"the area of triangle is  :{result_area}")
