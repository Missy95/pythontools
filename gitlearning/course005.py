import random
# 分支结构
# x = float(input('请输入x：'))
# if x < 5:
#     y = x + 3
# elif 5 < x < 10:
#     y = 2 * x
# else:
#     y = 10
# print(f'f({x})={y}')

# 循环结构
# 求1-100的和 for in
# total = 0
# for x in range(1, 101):
#     total += x
# print(total)

# 猜数字 while
# 产生一个1-100的随机数
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    num = int(input('请输入一个数：'))
    if num < answer:
        print('再大一点')
    elif num > answer:
        print('再小一点')
    else:
        print('恭喜你，猜对了')
        break
print(f'你总共踩了{counter}次')