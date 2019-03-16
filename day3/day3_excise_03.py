import pymysql
from config import DB_API_TEST

def change_db(conn,sql):
    # 1.建立连接
    # conn = get_conn()
    # 2.建立游标，作为一个缓冲区
    cur = conn.cursor()
    # 3.使用execute（）方法执行SQL语句
    cur.execute(sql)
    #4.提交更改
    conn.commit()
    #5.关闭连接
    conn.close()

def query_db(conn,sql):
    # 1.建立连接
    # conn = get_conn()
    # 2.建立游标，作为一个缓冲区
    cur = conn.cursor()
    # 3.使用execute（）方法执行SQL语句
    cur.execute(sql)
    # 4.获取数据
    # print(cur.fetchone())
    # print(cur.fetchone())
    # result = cur.fetchone()   # 取一条数据，还有一个fetchall（取所有），fetchmany（3）取3条
    # result1 = cur.fetchmany(3)  # 取三条数据，但是如果结果只有一个，那么这个就取不到结果
    result = cur.fetchall()    # 去所有数据
    # print(result[0]) # 元组取数据用[],从0开始对应第一个数据，
    # 5.关闭连接
    # conn.close()
    return result


def get_conn():
    conn = pymysql.connect(**DB_API_TEST)  # 拆包成六个数据
    return conn


if __name__ == "__main__":
    conn = get_conn()
    # print(query_db("SElECT * FROM USER where name = '马瑞雪';"))
    change_db('INSERT into user VALUES(70002,"李元","e10adc3949ba59abbe56e057f20f883e");')
    print(query_db("SElECT * FROM USER where id = 70002;"))
    conn.close()