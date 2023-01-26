import sqlite3

con = sqlite3.connect("q1.db")
print("Connected to SQLite")
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM customers WHERE grade > 200")
    rows = cur.fetchall()
    print(f"Total rows are:   {len(rows)}")

    print("Printing each row")
    for row in rows:
        print(f"Id:  {row[0]}",
              f"Name:  {row[1]}",
              f"City:  {row[2]}",
              f"Grade:  {row[3]}",
              f"Seller:  {row[4]}\n\n", sep='\n')

print("The SQLite connection is closed")
