'''SQLAIchemy
- 不需要书写SQL语句
- 不限于mysql数据库，还可以连接oracle / sqlite / sql server / postgresql / mysql
- 使用ORM
####### ORM
- Object：面向对象编程中的对象
- Relationship：关系，关系型数据库
- Mapper：映射
- 数据库中表和sqlqlchemy中的类映射，一张表对应一个类
- 类中的类属性和表中的字段映射，字段名和类变量名一样
- 表的每个字段都对应Column的一个实例
- 数据库中每种数据类型也都映射为一个sqlalchemy的类
- 类的实例，映射为表中的一行记录

'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#创建连接数据库的引擎


engine = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?选项
    'mysql+pymysql://root:123456@192.168.1.25/td1905?charset=utf8',
    encoding='utf8',
    # echo = True   # 显示调试信息，生产环境下不要设置
)

# 创建连接数据库的会话类
Session = sessionmaker(bind=engine)

# 生成实体类的基类
Base = declarative_base()

#类与表映射
class Departments(Base):
    __tablename__ = 'departments'   # 指定类对应的表
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20))
    birrh_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中没有表则创建，有的话只是进行关联，不会再创建一遍
    Base.metadata.create_all(engine)
