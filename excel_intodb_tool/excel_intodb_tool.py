import pandas as pd
from sqlalchemy import create_engine
import re
import pymysql
import sys
import time

# 默认为用户标签库配置
dbconfig = {'user': 'userprofile',
            'pwd': 'userprofile',
            'host': '172.31.24.50',
            'port': 3306,
            'database': 'userprofiledb'}


# 读取excel文件
def read_excel(path, colname):
    read = pd.read_excel(path, header=None, names=colname)
    return read


# 输入有误时重试函数
def retry_in(*arg):
    if arg[0] == 'case1':
        print('输入的库表名有误！请重新输入数据库和表名：', end='')
        newval = str(input())
        return check_dbtable(newval)
    elif arg[0] == 'case2':
        print('文件路径为空，请重新拖入!', end='')
        return into_db(arg[1], arg[2])


# 检查输入的库表是否正确
def check_dbtable(tbstr):
    # 通过.分割字符串
    tmp = tbstr.split('.')
    # 判断是否输入了库表
    if len(tmp) > 1:
        db = tmp[0]
        tb = tmp[1]
        try:
            conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['pwd'],
                                   db=db, port=dbconfig['port'], autocommit=True)
            curr = conn.cursor()
            tmp_db = "select * FROM information_schema.SCHEMATA WHERE SCHEMA_NAME ='%s'" % db
            curr.execute(tmp_db)
            # 获取结果集影响行数
            count_db = curr.rowcount
            # 检查数据库是否存在
            if count_db != 0:
                # 查不到表时 结果集返回的是空元组
                tmp_sql = "select * FROM information_schema.TABLES WHERE TABLE_NAME='%s'" % tb
                curr.execute(tmp_sql)
                # print(curr.fetchall())
                count_tb = curr.rowcount
                # 检查表是否存在
                if count_tb != 0:
                    # 查出表的所有列名 放入列表 排除掉自动增长的和有默认值的列
                    tmp_col = "select * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='%s' and TABLE_NAME='%s' " \
                              "and EXTRA!='auto_increment' and (IFNULL( COLUMN_DEFAULT, - 1 )= - 1 " \
                              "or COLUMN_DEFAULT = '') " \
                              "order by ORDINAL_POSITION " \
                              % (db, tb)
                    curr.execute(tmp_col)
                    data = curr.fetchall()
                    list1 = []
                    for filed in data:
                        list1.append(filed[3])
                    into_db(tb, list1)
                else:
                    retry_in('case1')
            else:
                retry_in('case1')
            curr.close()
            conn.close()
        except Exception as e:
            print('连接错误！')
            print(e)
            print('窗口将在15秒后自动关闭')
            time.sleep(15)
    else:
        retry_in('case1')


# 将数据插入数据库
def into_db(name, colist):
    connect_str = 'mysql+pymysql://%s:%s@%s:%d/%s' % \
                  (dbconfig['user'], dbconfig['pwd'], dbconfig['host'], dbconfig['port'], dbconfig['database'])
    # 连接数据库
    engine = create_engine(connect_str, encoding='utf8')
    try:

        print('请将要导入的文件拖动到此处：', end='')
        filepath = str(input())
        if filepath != '':
            readData = read_excel(filepath, colist)
            print('------------开始向%s表插入数据------------' % name)
            readData.to_sql(name, con=engine, index=False, if_exists='append')
            print('------------%s表插入数据成功！-------------' % name)
            print('窗口将在15秒后自动关闭')
            time.sleep(15)
        else:
            retry_in('case2', name, colist)

    except Exception as e:
        print('读取文件错误！')
        print(e)
        print('窗口将在15秒后自动关闭')
        time.sleep(15)
        # 文件读取错误 结束程序 避免执行插入异常后的语句
        sys.exit()


def typein_db(is_default):
    print('请输入要插入数据的数据库和表名：', end='')
    table_name = str(input())
    if is_default != 'Y' and judge != 'y':
        tmp = table_name.split('.')
        # 修改全局数据配配置的数据库字段为输入的数据库
        dbconfig['database'] = tmp[0]
        # 测试输入的内容是否能正确连接数据库
        try:
            con = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['pwd'],
                                  db=dbconfig['database'], port=dbconfig['port'], autocommit=True)
            con.close()
        except Exception as e:
            print('数据库连接错误！')
            print(e)
            custom_db()
    check_dbtable(table_name)


# 检查端口号是否为数字
def check_port():
    port = input()
    if port.isdigit():
        dbconfig['port'] = int(port)
    else:
        print('数据库端口号必须是数字！请重新输入：', end='')
        check_port()


# 自定义输入数据库配置
def custom_db():
    print('请输入数据库ip：', end='')
    dbconfig['host'] = str(input())
    print('请输入数据库端口号：', end='')
    check_port()
    print('请输入数据库用户名：', end='')
    dbconfig['user'] = str(input())
    print('请输入数据库密码：', end='')
    dbconfig['pwd'] = str(input())
    typein_db('N')


if __name__ == '__main__':
    print('*********************************************************************************')
    print('                           欢迎使用插数据工具')
    print('*********************************************************************************')
    print('''使用说明：
    1.选择是否使用默认配置，
    -要使用默认配置则输入Y（忽略大小写）；默认配置使用用户标签人群数据库，即userprofiledb库
    -不使用默认配置则输入N（忽略大小写）；需要手动输入其他数据库ip、端口号、用户名、密码等信息
    2.本工具仅能连接mysql数据库
    3.需要输入要插入数据的数据库名称和表名，输入格式为数据库名.表名，例如:userprofiledb.up_user_group_018
    4.需准备好数据文件，excel文件里按照DDL字段顺序填写数据，如有自增或有默认值的字段，无需填写，比如id、gmt_create等字段
    ''')
    print('是否用默认数据库配置 Y/N：', end='')
    judge = str(input())
    if judge != 'Y' and judge != 'y':
        custom_db()
    else:
        typein_db('Y')
