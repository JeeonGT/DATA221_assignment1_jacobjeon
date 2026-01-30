import math


def circle_area_comparison(radii_circle1, radii_circle2):
    if radii_circle1 > 0 and radii_circle2 > 0:
        area_circle1 = math.pi * (radii_circle1 ** 2)
        area_circle2 = math.pi * (radii_circle2 ** 2)
        if area_circle1 > area_circle2:
            area_circle_comparison_percentage = (area_circle2 / area_circle1)*100
            print(f"{area_circle_comparison_percentage}%")
        elif area_circle2 > area_circle1:
            area_circle_comparison_percentage = (area_circle1 / area_circle2)*100
            print(f"{area_circle_comparison_percentage}%")

    else:
        print("Your input must be a valid positive number.")

circle_area_comparison(8, 6)
