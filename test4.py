import pymysql
import datetime
import random
import numpy as np

test_config = {'host': 'localhost', 'user': 'root', 'password': 'root', 'port': 3306, 'db': 'testdb'}


# test_config = {'host': '172.31.24.50', 'user': 'marketing', 'password': 'marketing', 'port': 3306,
#                'db': 'marketing_portraitdb'}


def crete_data(line=10):
    conn = pymysql.connect(host=test_config['host'], user=test_config['user'], port=test_config['port'],
                           passwd=test_config['password'], db=test_config['db'])
    cur = conn.cursor()
    try:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # rad_num = str(random.randint(100000000, 199990999))
        data = [(now_time,now_time , -1, -1, -1, -1, str(random.randint(100000000, 199990999)), -1, -1, -1, 24260, 1) for i in range(0, line)]
        sql = "insert into user_province_precheck_job (gmt_modified,gmt_create,u_uid," \
              "user_id,product_id,agreement_no,mobile_num,is_paymember,province_id" \
              ",send_status,cur_month,part_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \

        # cur.execute(sql)
        # 第一种方法单条插入 使用for循环每次insert插入 比较耗时 第二种方法使用executemany 要把所有的占位符改为%s 否则会报错 源码里面都是转为字符串；如果使用第一种方法，则按照原来的类型匹配展位符即可
        cur.executemany(sql, data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    print('插入成功')
    cur.close()
    conn.close()


if __name__ == '__main__':
    print('请输入要插入的数据量：')
    line = int(input())
    crete_data(line)
