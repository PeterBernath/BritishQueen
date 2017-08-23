from flask import Flask, render_template, redirect, request, session
from collections import Counter


app = Flask(__name__)


counts = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}
counts = Counter(counts)


@app.route("/")
def route_index():
    return render_template("index.html")



@app.route("/request-counter", methods=["GET", "POST", "PUT", "DELETE"])
def count_request():
    count = 0
    if method == "PUT":
        count += 1
    print(count)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
