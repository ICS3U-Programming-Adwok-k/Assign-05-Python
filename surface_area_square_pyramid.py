#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 25th, 2025
"""
This program gets the base and height from the user, and then calculates the surface
are of a square pyramid and displays the calculated area in 2 decimal points
"""

import math


def surface_area(base_float, height_float):


    # Calculate the slant height
    slant_height = math.sqrt(math.pow(height_float, 2) + math.pow(base_float / 2, 2))

    # Calculate the base area
    base_area = math.pow(base_float, 2)

    # Calculate the area of one triangular face
    area_triangle = (base_float * slant_height) / 2

    """
    Calculate the total lateral area (area of all four triangular faces)
    """
    lateral_area = 4 * area_triangle

    # Calculate the total surface area
    surface_area = base_area + lateral_area

    return surface_area


def main():
    print("Hello and welcome to Adwok's math equation.")

    base_string = input("What is the base: ")
    height_string = input("What is the height: ")

    try:
        base = float(base_string)
        height = float(height_string)

        if base <= 0 and height <= 0:
            print("The base and height have to be positive numbers")
        elif base <= 0:
            print("The base has to be a positive number")
        elif height <= 0:
            print("The height has to be a positive number")
        else:
            calculated_area = surface_area(base, height)
            print(f"The surface area is: {calculated_area:.2f}")
    except ValueError:
        print("This is an invalid input")

    finally:
        print("Thank you for participating")


if __name__ == "__main__":
    main()
