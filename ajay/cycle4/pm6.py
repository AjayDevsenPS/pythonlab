
# Lambda function to calculate the area of a square
square_area = lambda side: side ** 2

# Lambda function to calculate the area of a rectangle
rectangle_area = lambda length, width: length * width

# Lambda function to calculate the area of a triangle
triangle_area = lambda base, height: 0.5 * base * height

# Get user input
side_length = float(input("Enter the side length of the square: "))
rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
triangle_base = float(input("Enter the base length of the triangle: "))
triangle_height = float(input("Enter the height of the triangle: "))

# Calculate and display the areas
print("Area of square:", square_area(side_length))
print("Area of rectangle:", rectangle_area(rectangle_length, rectangle_width))
print("Area of triangle:", triangle_area(triangle_base, triangle_height))

