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

    def __repr__(self):
        return f'Member {self.username}, {self.email}'


if __name__ == '__main__':
    app.run()

'''
query:
q1 = Member.query
q2 = q1.filter(Member.username == 'Marco')
q1.all()
q2.all()
# not equals and like
Member.query.filter(Member.username != 'Marco').all()
like_query = Member.query.filter(Member.username.like('%ch%')).all()
# in and not in 
q = Member.query.filter(Member.username.in_(['Marco', 'Echo'])).all()
q = Member.query.filter(~Member.username.in_(['Marco', 'Echo'])).all()
# null and not null
q = Member.query.filter(Member.email == None).all()
q = Member.query.filter(Member.email != None).all()
# and
q = Member.query.filter(Member.username == 'Marco').filter(Member.email == 'marco@demo.com').all()
q = Member.query.filter(Member.username == 'Marco', Member.email == 'marco@demo.com').all()
q = Member.query.filter(db.and_(Member.username == 'Marco', Member.email == 'marco@demo.com')).all()
# or
q1 = Member.query.filter(db.or_(Member.username == 'Marco', Member.username == 'Echo')).all()
# order by
Member.query.order_by(Member.username).all()
Member.query.order_by(Member.id).all()
q1 = Member.query.filter(db.or_(Member.username == 'Marco', Member.username == 'Echo'))
q1.all()
q1.order_by(Member.username).all()
# limit
Member.query.limit(2).all()
Member.query.order_by(Member.username).limit(2).all()
# offset
Member.query.offset(2).all()
Member.query.offset(2).limit(1).all()
# count
Member.query.count()
Member.query.filter(db.or_(Member.username == 'Marco', Member.username == 'Kar')).count()
# inequality
q = Member.query.filter(Member.id > 4).all()
q = Member.query.filter(Member.id >= 3).all()
q = Member.query.filter(Member.email < 't').all()
'''
