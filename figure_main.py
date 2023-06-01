# %%
import figure
# [fill this line]

myline = figure.line(-1, 1)

try:
    circle = figure.area_right_triangle(myline.get_width(), myline.get_height())
    print(circle)
except ValueError:
    print("please input positive number for width and heigth")

try:
    regular_triangle = figure.area_ellipse(myline.get_width(), myline.get_height())
    print(regular_triangle)
except ValueError:
    print("please input positive number for width and heigth")

try:
    square = figure.area_rectangle(myline.get_width(), myline.get_height())
    print(square)
except ValueError:
    print("please input positive number for width and heigth")