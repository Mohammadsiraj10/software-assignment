# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:39:01 2023

@author: @Mohammadsiraj.h
"""

# Function to find the shape of a regular polygon based on the number of sides
def identify_polygon_shape(num_sides):
    shapes = {
        3: "Triangle",
        4: "Square",
        5: "Pentagon",
        6: "Hexagon",
        
    }
    
    if num_sides in shapes:
        return shapes[num_sides]
    else:
        return "Invalid number of sides"

# Example usage:
num_of_sides = int(input("Enter the number of sides of the polygon: "))

# Identify the shape based on the given number of sides
identified_shape = identify_polygon_shape(num_of_sides)
print(f"The identified shape is: {identified_shape}")

