import pandas as pd
from sqlalchemy import create_engine

dbconfig = {'user': 'userprofile',
            'pwd': 'userprofile',
            'host': '172.31.24.50:3306',
            'database': 'userprofiledb'}


def read_excel():
    read = pd.read_excel('D:/MyData/人群.xlsx', header=None, names=['distinct_id', 'base_time', 'ext'])
    return read


if __name__ == '__main__':
    print('请输入要插入数据的表名：')
    table_name = str(input())
    connect_str = 'mysql+pymysql://%s:%s@%s/%s' % \
                  (dbconfig['user'], dbconfig['pwd'], dbconfig['host'], dbconfig['database'])
    # 连接数据库
    engine = create_engine(connect_str, encoding='utf8')
    try:
        readData = read_excel()
        readData.to_sql(table_name, con=engine, index=False, if_exists='append')
        print('插入数据成功！')
    except Exception as e:
        print(e)



