from flask import Flask
from flask_cors import CORS
import schedule_bot

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/schedule-scraping', methods=['POST'])
def start_scraping_bot():
    schedule_bot.schedule_scraping()
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82)