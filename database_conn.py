import sqlite3

class create_db:
    conn=sqlite3.connect('dance_feet.db')
    c=conn.cursor()

    # c.execute("""
    #     CREATE TABLE if not exists users(
    #     username text,
    #     password text,
    #     level integer
    # );
    # """)
    #
    # username = 'admin'
    # c.execute(f"SELECT * from users WHERE username='{username}'")
    # records = c.fetchall()
    # print(records)
    # if len(records) == 0:
    #     c.execute("INSERT INTO users VALUES('admin','123','3')")
    #     print("admin user added successfully to the database")
    # else:
    #     print("the admin login data is already exist")
