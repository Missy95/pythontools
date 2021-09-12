import pandas as pd
import pymysql
from sqlalchemy import create_engine


# readexcel = pd.read_excel('D:/MyData/数据.xlsx', header=None,names=['username','sex','phone','province'],skiprows=1)
# # 连接数据库
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/mysql?charset=utf8')
# readexcel.to_sql('person',con=engine,index=False,if_exists='append')

def read_excel():
    # read = pd.read_excel('D:/MyData/星火数据.xlsx', header=None, names=['spma', 'spmb', 'spmc', 'spmd', 'begin_time',
    #                                                                 'end_time', 'click_times', 'exposure_times',
    #                                                                 'source_url',
    #                                                                 'click_users', 'exposure_users', 'static_time_th',
    #                                                                 'click_times_th',
    #                                                                 'exposure_times_th', 'click_users_th',
    #                                                                 'exposure_users_th',
    #                                                                 'ad_idea_id', 'ad_unit_id'])
    read = pd.read_excel('D:/MyData/续订资格校验.xlsx', header=None, names=['u_uid', 'user_id', 'product_id', 'agreement_no',
                                                                    'mobile_num', 'is_paymember', 'province_id',
                                                                    'send_status','cur_month'
                                                                   ])
    return read


if __name__ == '__main__':
    # 连接数据库
    # engine = create_engine('mysql+pymysql://bmpointcore:bmpointcore@172.31.24.50:3306/bmpointcore', encoding='utf8')
    engine = create_engine('mysql+pymysql://marketing:marketing@172.31.24.50:3306/marketing_portraitdb', encoding='utf8')
    readData = read_excel()
    readData.to_sql('user_province_precheck_renew_job', con=engine, index=False, if_exists='append')
    #ad_throw_data_statis
    print('插入完成')
