import time
import mysql.connector
from task import create

x = 1
"""
below you can see loop It is crucial because my code have to see mysql is started. 
After db has started, this loop will stop
"""
while x:
    try:
        db = mysql.connector.connect(
            user='root',
            host="db",
            password="Qwerty123$",
            port=3306,

            # database="mds"
        )
        x = 0
    except:
        x += 1
        time.sleep(3)
        pass

cursor = db.cursor()


"""
It is simple insert function. It has only insert, no perm or other checking
"""


def insert(sql):
    cursor.execute(sql)
    db.commit()


def write(data):
    sql = f"INSERT INTO mds.customers (group_code, group_desc, code, code_desc) VALUES ('{data.get('group_code')[0]}', '{data.get('group_desc')[0]}', '{data.get('code')[0]}','{data.get('code_desc')[0]}');"
    try:
        insert(sql)
        return True
    except mysql.connector.errors.ProgrammingError:
        """
        That error means database not found, code will redirect to create new database and table to another python file
        """
        if create(db):
            insert(sql)

        return True
