year = int(input("输入年份，四位整数："))

'''
year = (year - 1996) % 12

if year == 0:
    print('鼠')
elif year == 1:
    print('牛')
elif year == 2:
    print('虎')
elif year == 3:
    print('兔')
elif year == 4:
    print('龙')
elif year == 5:
    print('蛇')
elif year == 6:
    print('马')
elif year == 7:
    print('羊')
elif year == 8:
    print('猴')
elif year == 9:
    print('鸡')
elif year == 10:
    print('狗')
elif year == 11:
    print('猪')
'''

animals = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
print(animals[(year - 1996) % 12])
