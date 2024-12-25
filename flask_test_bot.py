from flask import Flask
from flask_cors import CORS
import test

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/test-bot', methods=['POST'])
def start_test_bot():
    test.run()
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=84)