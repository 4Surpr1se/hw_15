import sqlite3


with sqlite3.connect("./animal.db") as con:
    cur = con.cursor()
    sqlite_query = f"""
    
    """
    # скрипт sql в shows.txt
    result = cur.executescript(sqlite_query)
    executed_query = cur.fetchall()
    result = executed_query
    con.commit()
    print(result)

