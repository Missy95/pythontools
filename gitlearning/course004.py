# 华氏度转温度

# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 18
# print('%.1f华氏度等于%.f摄氏度' % (f, c))

# 输入圆的半径，计算周长和面积
# radius = float(input('请输入圆的半径：'))
# meter = 2 * 3.14 * radius
# area = 3.14 * radius * radius
# print('圆的周长为%f,半径为%f' % (meter, area))

# 判断输入年份是否为闰年
year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)