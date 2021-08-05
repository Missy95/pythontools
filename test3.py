import pandas as pd
import pymysql
from sqlalchemy import create_engine


# readexcel = pd.read_excel('D:/MyData/数据.xlsx', header=None,names=['username','sex','phone','province'],skiprows=1)
# # 连接数据库
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/mysql?charset=utf8')
# readexcel.to_sql('person',con=engine,index=False,if_exists='append')

def read_excel():
    read = pd.read_excel('D:/MyData/人群.xlsx', header=None, names=['distinct_id', 'base_time', 'ext'])
    return read


if __name__ == '__main__':
    # 连接数据库
    engine = create_engine('mysql+pymysql://userprofile:userprofile@172.31.24.50:3306/userprofiledb', encoding='utf8')
    readData = read_excel()
    readData.to_sql('up_user_group_020', con=engine, index=False, if_exists='append')
