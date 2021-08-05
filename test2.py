import pymysql

# 打开数据库连接
# db = pymysql.connect(host='localhost', user='root', passwd='root', db='mysql')
# # 获取数据库游标
# cursor = db.cursor()
# # 使用execute执行sql
# cursor.execute('select * from person')
# # 使用fetchall方法获取所有数据
# data = cursor.fetchall()
# print(data)
# db.close()

with open('D:/MyData/数据.xlsx', 'r',encoding='ISO-8859-1') as file:
    data_info = file.readlines()
    print(data_info)
