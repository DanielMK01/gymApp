import sqlite3

def create_db_table():
    con = sqlite3.connect("gymcache.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""CREATE TABLE gymdays(
                dow TEXT, 
                ename TEXT,
                FOREIGN KEY(ename) REFERENCES exercisedmuscle(ename))""")
    cur.execute("""CREATE TABLE exercisedmuscle(
                ename TEXT UNIQUE,
                musclegroup TEXT)""")
    con.close()

def add_em(ename, mname):
    try:
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.execute("INSERT INTO exercisedmuscle VALUES(?, ?)", {ename, mname})
        con.commit()
        con.close()
    except:
        print("An exception occurred in add_em()")

def add_em_from_file(edata, mdata):
    try:
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.executemany("INSERT INTO exercisedmuscle VALUES(?, ?)", {edata, mdata})
        con.commit()
        con.close()
    except:
        print("error on adding em from file")

def delete_em(ename, mname):
    try:
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.execute("DELETE FROM exercisedmuscle WHERE ename = ? AND mname = ?", {ename, mname})
        con.commit()
        con.close()
    except:
        print("An exception occurred in add_em()")

def add_exercise(dow, ename):
    try:
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.execute("INSERT INTO gymdays VALUES(?, ?)", dow, ename)
        con.commit()
        con.close()
    except:
        print("An exception occurred in add_exercise()")    

def clear_week():
    try:
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.execute("DELETE FROM gymdays;")
        con.commit()
        con.close()
    except:
        print("An exception occurred in clear_week()")