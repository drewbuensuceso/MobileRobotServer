#user = root
#pw = root

###Log system for the newly structured mobileRobotServer

import mysql.connector as mc
import pandas as pd

def db_connect():
    cnx = mc.connect(user='root', password='root',
                              host='localhost',
                              database='mobileRobotServer')
    return(cnx)


def execute_query(query):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        if "SELECT" in query:
            result = pd.read_sql(sql=query, con=conn)
        else:
            cursor.execute(query)

    except mc.Error as e:
        print(e)

    finally:
        return result, cursor.close(),conn.close()