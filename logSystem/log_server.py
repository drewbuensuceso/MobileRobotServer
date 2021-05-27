import os.path
from numpy import tracemalloc_domain
import pandas as pd
import db
from flask import Flask, render_template, url_for

app = Flask(__name__)
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


@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')

@app.route('/logs', methods=['GET'])
def logs():
    return render_template('logs.html', logs=read_log())

@app.route('/verification', methods=['GET'])
def verification():
    return render_template('verification.html', logs=read_log())

@app.route('/statements', methods=['GET'])
def statements():
    return render_template('statements.html', logs=read_log())
    

if __name__ == "__main__":
    #generate_file("192.168.88.25", "xxxx-jake-0876", "123124123", "sxs1223")
    #print(read_log(50))
    #print(datetime.now())
    ##verification("thisisadummyvcimgstring", "aw121", "xx-Ray-xx", "123124123", "192.168.88.25", "2021-05-25 12:25:03")
    ##verification("thisisadummyvcimgstring", "aw121", "xx-Ray-xx", "123124123", "192.168.88.25", "2021-05-25 12:25:03")
    app.run(host='0.0.0.0', port=port, debug=True)
