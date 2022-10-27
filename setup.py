import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('apples')")
cursor.execute("insert into list (description) values ('orange')")
cursor.execute("insert into list (description) values ('mango')")
cursor.execute("insert into list (description) values ('pineapple')")
cursor.execute("insert into list (description) values ('grapes')")

connection.commit()
connection.close()

print("done.")