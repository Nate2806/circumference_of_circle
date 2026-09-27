#IMPORTING LIBRARY
import math

user_radius=eval(input("Enter the radius of your circle:"))
#DEFINING RADIUS
def calc_circumference(radius):
    circumference= 2*math.pi*radius #FUNCTION BODY

    return circumference

print("The circumference of the circle is:", calc_circumference(user_radius)) # Function Call
