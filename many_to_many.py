from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    email = db.Column(db.String(30))
    join_date = db.Column(db.DateTime)
    orders = db.relationship('Order', backref='member', lazy='dynamic')
    courses = db.relationship('Course', secondary='user_courses', backref='member', lazy='dynamic')

    def __repr__(self):
        return f'Member {self.username}, {self.email}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('member.id'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

db.Table('user_courses',
    db.Column('user_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    )



if __name__ == '__main__':
    app.run()
    
'''
course1 = Course(name='Course One')
course2 = Course(name='Course Two')
course3 = Course(name='Course Three')
marco = Member.query.filter(Member.username == 'Marco').first()
echo = Member.query.filter(Member.username=='Echo').first()
course1.member.append(marco)
course1.member.append(echo)
course2.member.append(marco)
marco.courses.all()
course1.member
'''