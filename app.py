from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to flask api"

if __name__ == '__main__':
    app.run(debug=True)