from flask import Flask, jsonify

check_app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    check_app.run()
