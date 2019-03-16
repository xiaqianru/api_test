'''数据库封装方法'''
import pymysql
from config import DB_API_TEST,DB_longtengserver


def get_conn(db_conf=DB_API_TEST):   # 默认值
    conn = pymysql.connect(**db_conf)
    return conn


def query_db(conn, sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return result


def change_db(conn, sql):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as ex:
        conn.rollback()

if __name__ == "__main__":
    conn1 = get_conn(DB_longtengserver)  # 可以使用第二个配置的数据库
    conn = get_conn(DB_API_TEST)
    change_db(conn,'INSERT into user VALUES(70006,"李元","e10adc3949ba59abbe56e057f20f883e");')
    print(query_db(conn,"SELECT * from user WHERE id = 70006"))
    conn.close()
