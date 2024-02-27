from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    total_points = db.Column(db.Integer)
    orders = []

    def delete(self):
        db.session.delete(self)

    def addPoints(self, points):
        self.total_points += int(points)

    def removePoints(self, points):
        self.total_points -= int(points)

    def addOrder(self, order):
        self.orders.append(order)


class Order:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id
