# Importing specific modules and functions
from graphics.rectangle import area as rect_area
from graphics.circle import perimeter as circ_perimeter
from graphics.threeDgraphics.cuboid import volume as cuboid_volume
from graphics.threeDgraphics.sphere import surface_area as sphere_surface_area

# Importing all functions from a module
from graphics.circle import *

# Importing a sub-package
from graphics.threeDgraphics import sphere



# Using the imported functions

breadth=int(input("Enter the breadth of the rectangle:"))
length=int(input("Enter the length of the rectangle:"))
print("Rectangle Area:", rect_area(breadth,length))

radius=int(input("Enter the radius of the circle:"))
print("Circle Perimeter:", circ_perimeter(radius))
# Using functions from the selectively imported module
print("Circle Area:", area(radius))  # This is from the selectively imported circle module

len=int(input("Enter the length of the cuboid:"))
wid=int(input("Enter the width of the cuboid:"))
hei=int(input("Enter the height of the cuboid:"))

print("Cuboid Volume:", cuboid_volume(len, wid, hei))

rad=int(input("Enter the sphere's radius:"))
print("Sphere Surface Area:", sphere_surface_area(rad))

