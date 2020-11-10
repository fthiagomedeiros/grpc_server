from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_health():
    method = request.method
    return jsonify({'message': 'HTTPs', 'request': method})


if __name__ == '__main__':
    app.run()
