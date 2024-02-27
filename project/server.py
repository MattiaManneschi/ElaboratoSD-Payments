from flask import Flask, render_template

app = Flask(__name__)

my_id = "server_id"


@app.route("/get_data", methods=["GET", "POST"])
def get_data(price):
    price = processPrice(price)
    return render_template("buy_order.html", id=my_id, price=price)


def processPrice(price):
    price = price.replace("€", "")
    price.strip()
    price = float(price)
    price = float("{:.2f}".format(price))
    return price


if __name__ == '__main__':
    app.run(debug=True)
