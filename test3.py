import pandas as pd
import pymysql
from sqlalchemy import create_engine


# readexcel = pd.read_excel('D:/MyData/数据.xlsx', header=None,names=['username','sex','phone','province'],skiprows=1)
# # 连接数据库
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/mysql?charset=utf8')
# readexcel.to_sql('person',con=engine,index=False,if_exists='append')

def read_excel():
    read = pd.read_excel('D:/MyData/星火数据.xlsx', header=None, names=['spma', 'spmb', 'spmc', 'spmd', 'begin_time',
                                                                    'end_time', 'click_times', 'exposure_times',
                                                                    'source_url',
                                                                    'click_users', 'exposure_users', 'static_time_th',
                                                                    'click_times_th',
                                                                    'exposure_times_th', 'click_users_th',
                                                                    'exposure_users_th',
                                                                    'ad_idea_id', 'ad_unit_id'])
    return read


if __name__ == '__main__':
    # 连接数据库
    engine = create_engine('mysql+pymysql://bmpointcore:bmpointcore@172.31.24.50:3306/bmpointcore', encoding='utf8')
    readData = read_excel()
    readData.to_sql('ad_throw_data_statis', con=engine, index=False, if_exists='append')
    print('插入完成')
