import sqlite3

# Setup connection to DB with inforced constraints
db = sqlite3.connect('data/db.db')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Create user table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user(
              usr_id INTEGER PRIMARY KEY NOT NULL,
              usr_name TEXT UNIQUE NOT NULL ,
              usr_pswd TEXT NOT NULL )
''')

# Create msg table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS msg(
              mgs_id INTEGER PRIMARY KEY NOT NULL ,
              msg TEXT NOT NULL ,
              usr_id INTEGER NOT NULL ,
              FOREIGN KEY (usr_id) REFERENCES user(usr_id))
''')


# # Insert user
# username = "username"
# user_password = "1234"
# try:
#     cursor.execute('''INSERT INTO user(usr_name, usr_pswd)
#                       VALUES(?,?)''', (username, user_password))
# except sqlite3.IntegrityError as er:  # We expect an error if username already exist
#     print("User doesn't exist")
#
# # Insert message
# id = 3
# message = "Hello world"
# try:
#     # if py_msg is "":  # deprecated
#     #     raise Exception
#     cursor.execute('''INSERT INTO msg(msg, usr_id) VALUES(?,?)''', (message, id))
# except Exception as e:  # We don't expect an error here.
#     print(e)

# Prints all users
cursor.execute("SELECT * FROM user")
all_rows = cursor.fetchall()
print("Users", all_rows)
# Prints all messages
cursor.execute("SELECT * FROM msg")
all_rows = cursor.fetchall()
print("Messages", all_rows)
# Prints messages of user by id
id = 2
cursor.execute("SELECT * FROM msg WHERE usr_id=?", (id,))
print(f"Messages of user {id}", cursor.fetchall())


db.commit()
db.close()
