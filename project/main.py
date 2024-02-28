import random
import string

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from project.server import get_data
from . import db
from .models import Order

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    orders = []
    for i in range(len(current_user.orders)):
        orders = current_user.orders[i].id
    return render_template('profile.html', name=current_user.name, orders=orders)


@main.route('/purchase', methods=['POST', 'GET'])
@login_required
def purchase():
    return render_template('purchase.html', name=current_user.name, total_points=current_user.total_points)


@main.route('/wallet', methods=['GET'])
@login_required
def wallet():
    return render_template('wallet.html', name=current_user.name, total_points=current_user.total_points)


@main.route('/callServer', methods=['POST', 'GET'])
def callServer():
    global points
    points = request.form['tag']
    price = request.form['price']
    return get_data(price)


@main.route('/addPoints', methods=['POST', 'GET'])
@login_required
def addPoints():
    current_user.addPoints(int(points))
    db.session.commit()
    return render_template("index.html")


@main.route('/buy', methods=['POST', 'GET'])
@login_required
def buy_order():
    return render_template('buy_order.html')


@main.route('/order', methods=['POST', 'GET'])
def removePoints():
    r_p = request.form['tag']
    current_user.removePoints(r_p)

    new_order = Order(id=generateCode(10), user_id=current_user.id)

    current_user.addOrder(new_order)

    db.session.commit()
    return render_template('index.html')


@main.route('/KO', methods=['POST', 'GET'])
def ko():
    return render_template("ko.html")


@main.route('/aboutUs', methods=['POST', 'GET'])
def aboutUs():
    return render_template("aboutUs.html")


def generateCode(length):
    characters = string.ascii_lowercase

    return ''.join(random.choices(characters, k=length))
