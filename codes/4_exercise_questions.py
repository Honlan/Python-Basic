color = input("我最喜欢的颜色：")
color1 = "蓝色"
gender = input("我的性别：")
gender1 = "男"
fruit = input("我最喜欢的水果：")
fruit1 = "西瓜"
birth = input("我的生日，例如03.26：")
birth1 = "03.26"
game = input("我最喜欢的游戏：")
game1 = "王者荣耀"

score = 0

if color == color1:
    score = score + 1
    # score += 1
if gender == gender1:
    score += 1
if fruit == fruit1:
    score += 1
if birth == birth1:
    score += 1
if game == game1:
    score += 1

print(score)

if score == 5:
    print('5 分')
elif score == 4:
    print('4 分')
elif score == 3:
    print('3 分')
elif score == 2:
    print('2 分')
elif score == 1:
    print('1 分')
elif score == 0:
    print('0 分')
    
