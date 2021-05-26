import db
import pandas as pd
from flask import Flask, render_template 

app = Flask(__name__)
port = 8686

def create_log(log, accountAlias, device):
    query = "INSERT INTO logs VALUES {LOG}, {ACCOUNT_ALIAS}, {DEVICE}".format(LOG=log, ACCOUNT_ALIAS=accountAlias, DEVICE=device)
    return db.execute_query(query)

def delete_log(log_id,device):
    query = "DELETE FROM logs WHERE log_id = {logId}".format(logId=log_id)
    return db.execute_query(query)

def read_log(limit=50):
    query = "SELECT * FROM logs LIMIT {numlimit}".format(numlimit=limit)
    data = db.execute_query(query)
    return data


@app.route('/logs', methods=['GET'])
def logs_index():
    return render_template('index.html', logs=read_log())
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)