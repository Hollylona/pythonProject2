import sqlite3

con = sqlite3.connect('base.db')
cursor = con.cursor()
cursor.execute("""create table fruits(name text, color text, price int)""")
cursor.execute("""insert into fruits(name, color, price) values ('lime', 'green', 6)""")
cursor.execute("""insert into fruits(name, color, price) values ('apple', 'green', 3)""")
cursor.execute("""insert into fruits(name, color, price) values ('orange', 'red', 3)""")
con.commit()


con.close()


