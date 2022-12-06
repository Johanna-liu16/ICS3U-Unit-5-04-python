#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program converts grades

import math


def calculate_volume(radius: int, height: int) -> str:
    # calculate volume
    volume = math.pi * radius**2 * height
    return volume


def main():
    # input
    print("This program calculates the volume of a cylinder.")
    str_radius = input("Enter length of radius (cm): ")
    str_height = input("Enter length of height (cm): ")

    try:
        radius = int(str_radius)
        height = int(str_height)
        # call functions
        total_volume = calculate_volume(radius, height)
        print(
            "Volume of a cylinder with a radius of {0} cm and a height of {1} cm is {2}cm³".format(
                radius, height, round(total_volume, 2)
            )
        )
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
