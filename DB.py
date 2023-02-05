import psycopg2
import datetime as dt

def connect_to_db():
    conn = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "qwerty",
        host = "localhost",
        port = 5432
    )
    return conn

def add_client(teleg_id,nickname,phonenumber):
    conn = connect_to_db()
    cur = conn.cursor()
    insert_into ="""insert into "Client" ("ClientId","Nick","DateRegistered","TelephoneNumber") values (%s,%s,%s,%s)"""
    cur.execute(insert_into,(teleg_id,nickname,dt.datetime.now(),phonenumber))
    conn.commit()
    cur.close()

def add_fio(client_id,FIO):
    conn = connect_to_db()
    cur = conn.cursor()
    update = """update "Client" set "Name"=%s where "ClientId"=%s"""
    cur.execute(update,(FIO,client_id))
    conn.commit()
    cur.close()

"""
class Order:
    def __init__(self,teleg_id):
        self.client_id = teleg_id
        self.order_list = []
        self.order_time = None

order = Order(123123123)
print(vars(order))
"""


