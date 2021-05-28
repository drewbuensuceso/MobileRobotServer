#user = root
#pw = root

###Log system for the newly structured mobileRobotServer

import mysql.connector as mc
import pandas as pd
import json 

def db_connect():
    cnx = mc.connect(user='root', password='password',
                              host='localhost',
                              database='mobileRobotServer')
    return(cnx)


def execute_query(query):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute(query)
        if 'SELECT' in query:
            row_headers=[x[0] for x in cursor.description]
            rv = cursor.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        conn.commit()
    except mc.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


    return json_data
