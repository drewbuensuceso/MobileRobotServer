import os.path
from numpy import tracemalloc_domain
import pandas as pd
import db
from flask import Flask, render_template, url_for,request, session
import datetime

app = Flask(__name__)
app.secret_key = 'logsystemsecret'
port = 8686

SAVE_PATH = "../devices/"
# {[IP:"192.168.88.10", accountAlias="xxxx-jake-0876", device="123124123"]} #sample request file output

def generate_deviceInfo(ipaddr, accountAlias, device, device_id):
    file_path = os.path.join(SAVE_PATH, device_id + ".json")
    req_dict = pd.DataFrame([[ipaddr, accountAlias, device]], columns=['ip', 'accountAlias', 'device'])
    req_dict.to_json(file_path, orient="records")

def txt(txtLog, accountAlias, device, ip_address, transTime): #logs transaction texts
    columns = "trans_time, accountAlias, device_id, ip_address, log, log_type"
    values = transTime, accountAlias, device, ip_address, txtLog, "txt"
    query = "INSERT INTO logs ({COLUMNS}) VALUES {VALUES}".format(COLUMNS=columns, VALUES=values)
    try:
        db.execute_query(query)
        code = 0
        msg = "success"
        return code, msg
    except:
        code = 1
        msg = "failed to insert log text"
        return code, msg

def img(txtLog,transImg, accountAlias, device, ip_address, transTime): #logs transaction images
    columns = "trans_time, accountAlias, device_id, ip_address, img, log, log_type"
    values = transTime, accountAlias, device, ip_address, transImg, txtLog, "img"
    query = "INSERT INTO logs ({COLUMNS}) VALUES {VALUES}".format(COLUMNS=columns, VALUES=values)
    try:
        db.execute_query(query)
        code = 0
        msg = "success"
        return code, msg
    except:
        code = 1
        msg = "failed to transaction log image"
        return code, msg

def keyboard(keyboardImg, code, position, accountAlias, device, ip_address, transTime):
    #code = password
    #position = how to type it in the current keyboard
    columns = "trans_time, accountAlias, device_id, ip_address, img, code, position, log_type"
    values = transTime, accountAlias, device, ip_address, keyboardImg, code, position, "keyb_verification"
    query = "INSERT INTO logs ({COLUMNS}) VALUES {VALUES}".format(COLUMNS=columns, VALUES=values)
    try:
        db.execute_query(query)
        code = 0
        msg = "success"
        return code, msg
    except:
        code = 1
        msg = "failed to log keyboard"
        return code, msg

def verification(verificationImg, code, accountAlias, device, ip_address, transTime): #logs verificationImage-related images and string
    columns = "trans_time, accountAlias, device_id, ip_address, img, code, log_type"
    values = transTime, accountAlias, device, ip_address, verificationImg, code, "img_verification"
    query = "INSERT INTO logs ({COLUMNS}) VALUES {VALUES}".format(COLUMNS= columns, VALUES=values)
    try:
        db.execute_query(query)
        code = 0
        msg = "success"
        return code, msg
    except:
        code = 1
        msg = "failed to log verification code"
        return code, msg

def delete_log(log_id,device): #deletes a log by id
    query = "DELETE FROM logs WHERE log_id = {logId}".format(logId=log_id)
    return db.execute_query(query)

def read_log(limit=50):
    query = "SELECT * FROM logs LIMIT {numlimit}".format(numlimit=limit)
    data = db.execute_query(query)
    return data

@app.route('/set_lang', methods=['POST'])              
def set_lang():
    language_list = {
        'en': {
            'lang': 'English',
            'title': 'Log',
            'device': 'Devices',
            'statements': 'Statements',
            'verification': 'Verification',
            'transactions': 'Transactions',
            'update': 'Update',
            'diskspace': 'Disk Space'
        },
        'cn': {
            'lang': 'Chinese',
            'title': 'Log CN',
            'device': 'Devices CN',
            'statements': 'Statements CN',
            'verification': 'Verifications CN',
            'transactions': 'Transactions CN',
            'update': 'Update CN',
            'diskspace': 'Disk Space CN'
        },

    }
    language = request.form['lang']
    session['language'] = language_list[language.lower()]

    return {'success': True}


@app.route('/', methods=['GET'])              
def index():
    session['language'] = {
        'en': {
            'lang': 'English',
            'title': 'Log',
            'device': 'Devices',
            'statements': 'Statements',
            'verifications': 'Verifications',
            'transactions': 'Transactions',
            'update': 'Update',
            'diskspace': 'Disk Space'
        }
    }
    return render_template('base.html')

@app.route('/capture_device', methods=['POST'])
def capture_device():
    data = request.form
    now = datetime.datetime.now()
    
    txt(data.get('log', ''), data.get('accountAlias', ''), data.get('device_id', ''), data.get('ip', ''), now.strftime('%Y-%m-%d %H:%M:%S') )
    return {'message': 'success'}


@app.route('/logs', methods=['GET'])
def logs():
    print(session, '<==== SESSION')
    return render_template('logs.html', logs=read_log())

@app.route('/verification', methods=['GET'])
def verification():
    return render_template('verification.html', logs=read_log())

@app.route('/statements', methods=['GET'])
def statements():
    return render_template('statements.html', logs=read_log())

@app.route('/diskspace', methods=['GET'])
def diskspace():
    return render_template('diskspace.html')

@app.route('/upgrade', methods=['GET'])
def upgrade():
    data = [
        {
            "appName": "asistant app",
            "softwareNo": 13,
            "softwareVersion": 5,
            "imageURL": "static/images/boc.jpeg"
        },
        {
            "appName": "BOC bank",
            "softwareNo": 13,
            "softwareVersion": 5,
            "imageURL": "static/images/boc.jpeg"
        }
    ]
    return render_template('update.html', data=data)

@app.route('/transactions', methods=['GET'])
def transactions():
    transactions = [
        {
            "_id": 1,
            "token": "",
            "bankAccount": "xxxx-jake-0876",
            "balance": "5000000000",
            "trans": [
                    {
                        "transType": "1",
                        "transAmount": "12312312",
                        "name": "ray",
                        "balance": "5000000000",
                        "postscript": "for loan",
                        "customerAccount": "8838",
                        "branch": "makati",
                        "extensions": {
                            "mode": "",
                            "summary": "",
                            "channel": "",
                            "card": "BOC"
                        },
                        "transTime": datetime.datetime.now()
                    },
                    {
                    "transType": "2",
                    "transAmount": "12312312",
                    "name": "payne",
                    "balance": "1000000",
                    "postscript": "for credit",
                    "customerAccount": "1234",
                    "branch": "legaspi",
                    "extensions": {
                        "mode": "",
                        "summary": "",
                        "channel": "",
                        "card": "CCB"
                    },
                    "transTime": datetime.datetime.now()
                },
                {
                    "transType": "2",
                    "transAmount": "2131231",
                    "name": "ray",
                    "balance": "25.55",
                    "postscript": "payment",
                    "customerAccount": "5678",
                    "branch": "manila",
                    "extensions": {
                        "mode": "",
                        "summary": "",
                        "channel": "",
                        "card": "BOC"
                    },
                    "transTime": datetime.datetime.now()
                },
                {
                    "transType": "1",
                    "transAmount": "5552",
                    "name": "ray",
                    "balance": "1231231",
                    "postscript": "for loan",
                    "customerAccount": "5542",
                    "branch": "pasig",
                    "extensions": {
                        "mode": "",
                        "summary": "",
                        "channel": "",
                        "card": "CCB"
                    },
                    "transTime": datetime.datetime.now()
                }
            ]    
        }
    ]
    return render_template('transactions.html', transactions=transactions)
    

if __name__ == "__main__":
    #generate_file("192.168.88.25", "xxxx-jake-0876", "123124123", "sxs1223")
    #print(read_log(50))
    #print(datetime.now())
    ##verification("thisisadummyvcimgstring", "aw121", "xx-Ray-xx", "123124123", "192.168.88.25", "2021-05-25 12:25:03")
    ##verification("thisisadummyvcimgstring", "aw121", "xx-Ray-xx", "123124123", "192.168.88.25", "2021-05-25 12:25:03")
    app.run(host='0.0.0.0', port=port, debug=True)
