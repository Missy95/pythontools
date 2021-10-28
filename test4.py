import pymysql
import datetime
import random


def crete_data(line=10):
    conn = pymysql.connect(host='localhost', user='root', passwd='root', port=3306, db='testdb')
    cur = conn.cursor()
    now_time = datetime.datetime.now()
    rad_num = random.randint(100000000, 199990999)
    for i in range(0, line):
        sql = 'insert into user_province_precheck_job (\'gmt_modified\',\'gmt_create\',\'u_uid\',' \
              '\'user_id\',\'product_id\',\'agreement_no\',,\'mobile_num\',\'is_paymember\',\'province_id\'' \
              ',\'send_status\',\'cur_month\',\'part_id\') values(%s,%s,%s,%s,%s,%s,%s,%d,%d,%d,%d,%d)' % \
              (now_time, now_time, -1, -1, -1, -1, rad_num, -1, -1, -1, 24260, 1)


if __name__ == '__main__':
    print('请输入要插入的数据量：')
    line = input(int())
    crete_data(line)
