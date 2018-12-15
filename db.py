import sqlite3

class database:
    def __init__(self):
        # Setup connection to DB with inforced constraints
        global db
        db = sqlite3.connect('data/db.db')
        global cursor
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;") # PRAGMA (from pragmatic) is a directive.

        # Create user table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS usr(
                      usr_id INTEGER PRIMARY KEY NOT NULL,
                      usr_name TEXT UNIQUE NOT NULL ,
                      usr_pswd TEXT NOT NULL )
        ''')

        # Create msg table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS msg(
                      msg_id INTEGER PRIMARY KEY NOT NULL ,
                      msg TEXT NOT NULL ,
                      usr_id INTEGER NOT NULL ,
                      FOREIGN KEY (usr_id) REFERENCES usr(usr_id))
        ''')


def getallmessages():
    # cursor.execute("SELECT * FROM msg")
   #  cursor.execute('''select msg_id, msg, usr_id from msg
   # inner join usr on msg.usr_id = usr.usr_id''')

    cursor.execute('''
    select *
    from msg
    inner join (SELECT usr_name, usr_id from usr) usr 
    where usr.usr_id = msg.usr_id
''')

    temp_payload = cursor.fetchall()
    db.commit()
    db.close()

    finalpayload = {"msgs": []}

    for i in temp_payload:
        temp_msg = {}
        temp_msg["msg_id"] = i[0]
        temp_msg["msg_text"] = i[1]
        temp_msg["usr_id"] = i[2]
        temp_msg["usr_name"] = i[3]
        finalpayload["msgs"].append(temp_msg)

    return finalpayload



def getUser(usr_name, usr_pswd):

    try:
        cursor.execute(f"select * from usr where usr_name = '{usr_name}' and usr_pswd = '{usr_pswd}'")
        sqldata = cursor.fetchall()

        payload = {}
        payload["usr_id"] = sqldata[0][0]
        payload["usr_name"] = sqldata[0][1]
        payload["usr_pswd"] = sqldata[0][2]
    except:
        payload = {}

    db.commit()
    db.close()
    return payload


# createUser takes a dict
def createuser(dict):
    values_to_insert = [(dict.get('usr_name'), dict.get('usr_pswd'))]

    cursor.executemany('''
    insert into usr('usr_name','usr_pswd')
    values (?,?)''', values_to_insert)

    db.commit()
    db.close()


def createmessage(dict):
    values_to_insert = [(dict.get('msg'), dict.get('usr_id'))]

    cursor.executemany('''
     insert into msg('msg', 'usr_id')
     values (?,?)''', values_to_insert)

    db.commit()
    db.close()


