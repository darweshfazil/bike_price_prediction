from flask import Flask, render_template , request

import predict as p

app = Flask(__name__)

cost = 0

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method=="POST":
        global cost
        brand = request.form["brand"]
        power = request.form["power"]
        kms = request.form["kms"]
        year = request.form["year"]
        owner = request.form["owner"]

        cost_predict = p.price_prediction(brand,power, kms, year, owner)
        cost = cost_predict

    return render_template("bike.html", c=int(cost))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
