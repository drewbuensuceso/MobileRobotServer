import db
import pandas as pd

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
    print(read_log(50))