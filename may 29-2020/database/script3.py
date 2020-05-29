import sqlite3

def create_table(): 
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()



def insert(item, quantity, price ): 
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()
create_table()
insert("water glass",500,20000)


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    return rows
    conn.close()

print(view())