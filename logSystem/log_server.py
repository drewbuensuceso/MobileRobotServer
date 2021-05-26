import os.path
import pandas as pd
import db

SAVE_PATH = "../devices/"
# {[IP:"192.168.88.10", accountAlias="xxxx-jake-0876", device="123124123"]} #sample request file output

def generate_deviceInfo(ipaddr, accountAlias, device, device_id):
    file_path = os.path.join(SAVE_PATH, device_id + ".json")
    req_dict = pd.DataFrame([[ipaddr, accountAlias, device]], columns=['ip', 'accountAlias', 'device'])
    req_dict.to_json(file_path, orient="records")

def create_log(log, accountAlias, device):
    query = "INSERT INTO logs VALUES {LOG}, {ACCOUNT_ALIAS}, {DEVICE}".format(LOG=log, ACCOUNT_ALIAS=accountAlias, DEVICE=device)
    return db.execute_query(query)

def delete_log(log_id,device):
    query = "DELETE FROM logs WHERE log_id = {logId}".format(logId=log_id)
    return db.execute_query(query)

def read_log(limit):
    query = "SELECT * FROM logs LIMIT {numlimit}".format(numlimit=limit)
    data = db.execute_query(query)
    return data

if __name__ == "__main__":
    #generate_file("192.168.88.25", "xxxx-jake-0876", "123124123", "sxs1223")
    print(read_log(50))