'''PyMySQL应用
连接mysql数据库进行操作
此程序主要创建表

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

#编写创建表的SQL语句
create_dep = '''create table departments(
dep_id INT ,
dep_name VARCHAR (20),
PRIMARY KEY (dep_id)
)'''

create_emp ='''create table employees(
emp_id INT ,
emp_name VARCHAR (20),
birth_date DATE ,
email VARCHAR (50),
dep_id INT,
PRIMARY KEY (emp_id),
FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
)'''

create_sal = '''create table salary(
id INT ,
emp_id INT ,
date DATE ,
basic INT ,
awards INT ,
PRIMARY KEY (id),
FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)'''

#执行SQL语句
cur.execute(create_dep)
cur.execute(create_emp)
cur.execute(create_sal)

#对数据库有改动,需要确认
conn.commit()

#关闭游标
conn.close()
#关闭连接
cur.close()
