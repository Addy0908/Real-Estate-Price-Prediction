from flask import Flask, request, jsonify
app = flask.Flask(__name__)


@app.route('/hello')
def hello():
    return "HI"


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    app.run()
