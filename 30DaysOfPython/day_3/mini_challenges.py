#create a code that find the perimeter and/or area of a triangle
"""
def findArea(h,b):
    area = (h*b)/2
    return area

def findPerimeter(b,one,two):
    perimeter = (b+one+two)
    return perimeter

height = float(input("Height: "))
base = float(input("Base: "))
side_1 = float(input("Side length one: "))
side_2 = float(input("Side length two: "))
y = 0

area_perim = input("Type 'area' or 'perimeter: ")

while y == 0:
    if area_perim == "area":
        print("The area is",findArea(height,base),".")
        y = 1
    elif area_perim == "perimeter":
        print("The perimeter is",findPerimeter(base,side_1,side_2),".")
        y = 1
    else:
        print("Invalid input, try again.")
"""

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#find the zeros of a quadratic equation, find the y intercepts

#equation = complex(input("Input a standard form quadratic: "))
equation = j**2 + 5j + 6