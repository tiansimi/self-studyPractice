__author__ = 'lenovo'
from flask_sqlalchemy import SQLAlchemy
from flk import flaskapp

flaskapp.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev:fjrUWqUp4WVi8PE@101.124.9.171:3306/db_steward'
flaskapp.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(flaskapp.app)


class Role(db.Model):
    __tablename__ = 'role'  # 建立一个名字为:role的表
    id = db.Column(db.Integer, primary_key=True, autoincrement=False, nullable=False)
    name = db.Column(db.String(32), unique=True, nullable=False)


if __name__ == "__main__":
    # db.create_all()
    # 插入单挑数据
    # db.session.add(Role(name="zhangsan"))
    # db.session.commit()
    # 插入多条数据
    # users = [Role(name="lisa"), Role(name="米宝"), Role(name="Mommy"), Role(name="Daddy")]
    # db.session.add_all(users)
    #db.session.commit()
    users = Role.query.all()
    #print(users)
    #for user in users:
    #print(user)
    #print(user.id,user.name)
    #user1 = Role.query.first()
    #print(user1.name)
    #user2 = Role.query.filter_by(name = "米宝").first()   #多条件筛选就是name = **,id = **,逗号分隔
    #print(user2.name)
    user3 = Role.query.filter_by(name='米宝宝').first()
    print(user3)
    user3.name = "米乖乖"
    print(user3)
    db.session.commit()
















