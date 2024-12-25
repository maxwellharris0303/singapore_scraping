from flask import Flask
from flask_cors import CORS
import main_run_bot

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/run-bot', methods=['POST'])
def start_run_bot():
    main_run_bot.run()
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=83)