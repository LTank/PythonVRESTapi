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
    inner join (SELECT usr_name from usr) usr
''')


    payload = cursor.fetchall()
    db.commit()
    db.close()
    return payload



