import math
#Ask user to enter all 3 side
side1 = int(input("Please enter the 1st side of the triangle:"))
side2 = int(input("Please enter the 2nd side of the triangle:"))
side3 = int(input("Please enter the 3rd side of the triangle:"))

#calculate the area
s = (side1 + side2 + side3)/2
area = s*(s-side1)*(s-side2)*(s-side3)

#print the square root result
print(math.sqrt(area))