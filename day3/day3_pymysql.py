import pymysql

# 1.建立数据库连接
conn = pymysql.connect(host= '115.28.108.130',
                       port=3306,
                       user="test",
                       password="123456",
                       db="api_test",
                       charset="utf8")

# 2.建立游标，作为一个缓冲区
cur = conn.cursor()

# 3.使用execute（）方法执行SQL语句
cur.execute("SElECT * FROM USER where name = '马瑞雪';")

# 4.获取数据
# print(cur.fetchone())
# print(cur.fetchone())
result = cur.fetchone()   # 取一条数据，还有一个fetchall（取所有），fetchmany（3）取3条
result1 = cur.fetchmany(3)  # 取三条数据，但是如果结果只有一个，那么这个就取不到结果

print(result[0]) # 元组取数据用[],从0开始对应第一个数据，

# 5.关闭连接
conn.close()

