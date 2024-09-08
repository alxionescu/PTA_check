from flask import Flask, jsonify

check_app = Flask(__name__)

@check_app.route('/')
def index():
    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    check_app.run()
