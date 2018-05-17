def rect_cal(width, height):
    area = width * height
    zhouchang = (width + height) * 2
    return area, zhouchang

width = float(input('Please input the width: '))
height = float(input('Please input the height: '))

print(rect_cal(width, height))
