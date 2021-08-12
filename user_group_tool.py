import pandas as pd
from sqlalchemy import create_engine
import re

dbconfig = {'user': 'userprofile',
            'pwd': 'userprofile',
            'host': '172.31.24.50:3306',
            'database': 'userprofiledb'}


def read_excel():
    read = pd.read_excel('D:/MyData/人群.xlsx', header=None, names=['distinct_id', 'base_time', 'ext'])
    return read


def retry_in():
    print('输入的表名有误！请重新输入：')
    newval = str(input())
    return check_table(newval)


def check_table(tname):
    if tname.startswith('up_user_group_0'):
        lastwo = tname[15:]
        if lastwo != '' and len(lastwo) == 2:
            re_tname = re.compile(r'^[0-2][1-9]|[1-3]0')
            if re.match(re_tname, lastwo):
                into_db(tname)
            else:
                retry_in()
        else:
            retry_in()
    else:
        retry_in()


def into_db(name):
    connect_str = 'mysql+pymysql://%s:%s@%s/%s' % \
                  (dbconfig['user'], dbconfig['pwd'], dbconfig['host'], dbconfig['database'])
    # 连接数据库
    engine = create_engine(connect_str, encoding='utf8')
    try:
        print('------------开始向%s表插入数据------------' % name)
        readData = read_excel()
        readData.to_sql(name, con=engine, index=False, if_exists='append')
        print('------------------插入数据成功！------------------')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print('请输入要插入数据的表名：')
    table_name = str(input())
    check_table(table_name)
