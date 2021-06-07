from flask import Flask
import bank_bot
import requests


app = Flask(__name__)

@app.route('/post_device', methods=['GET'])
def post_device():
    device_info = bank_bot.post_device()
    response = requests.post('http://localhost:8686/capture_device', data=device_info.get('data', {}))
    return response.json()

@app.route('/xposed')
def bot():
    return bank_bot.xposed()

@app.route('/proxy', methods=['GET'])
def proxy():
    response = requests.get('https://www.google.com')
    return {'response': True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5023', debug=True)