'''PyMySQL应用
连接mysql数据库进行操作
此程序主要做增删改查操作


'''
'''导入模块pymysql'''
import pymysql

#创建到数据库服务器的连接
conn = pymysql.connect(
    host='192.168.1.25',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1905',
    charset='utf8'
)

#创建游标,通过游标对表操作
cur = conn.cursor()

#编写SQL语句

'创建部门(插入数记录)'
# insert1 = 'insert into departments VALUES (%s, %s)'
# hr = [('1','ha')]
# deps = [(2,'ops'), (3,'dev'), (4,'qa'), (5,'market'),(6,'sqles')]
# cur.executemany(insert1,hr)
# cur.executemany(insert1,deps)

'查询操作'
# select1 = 'select * from departments'
# cur.execute(select1)  #查询
# result1 = cur.fetchone()    #取一个记录
# print(result1)
# result2 = cur.fetchmany(2)   #取两个记录
# print(result2)
# result3 = cur.fetchall()  #  取出剩余的全部记录
# print(result3)

'移动游标'
# select1 = 'select * from departments'
# cur.execute(select1)
# cur.scroll(2,mode='absolute')
# result1 = cur.fetchone()
# print(result1)
# cur.scroll(1)
# result2 = cur.fetchone()
# print(result2)

'修改'
# update1 = 'update departments set dep_name=%s where dep_name=%s'
# cur.execute(update1,('hr','ha'))

'删除'
# delete1 = 'delete from departments WHERE dep_id=%s'
# cur.execute(delete1,6)

#执行SQL语句

#对数据库有改动,需要确认
conn.commit()

#关闭游标
conn.close()
#关闭连接
cur.close()
