from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30), default='password')
    email = db.Column(db.String(30))
    join_date = db.Column(db.DateTime)
    orders = db.relationship('Order', backref='member', lazy='dynamic')

    def __repr__(self):
        return f'Member {self.username}, {self.email}'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    def __repr__(self):
        return f"Member('{self.price}')"


if __name__ == '__main__':
    app.run()

'''
marco = Member.query.filter(Member.username == 'Marco').first()
order1 = Order(price=50, user_id=marco.id)
order2 = Order(price=20, member=marco)
first = marco.orders.first()
first.user_id
first.price
first.id
first.member
'''
