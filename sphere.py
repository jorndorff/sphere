




# You may not change anything below this line
# ---------- Main Program Below -------------

diameter = number_input("Please enter the diameter of a sphere in cm: ")
diameter = abs(diameter) # Absolute value to be sure diameter is positive.

radius = diameter / 2

circumference = sphere_circumference(radius)
area = sphere_area(radius)
volume = sphere_volume(radius)

print("\nThe circumference of your sphere is {} cm.".format(circumference))
print("The surface area of your sphere is {} cm2.".format(area))
print("The volume of your sphere is {} cm3.\n".format(volume))
