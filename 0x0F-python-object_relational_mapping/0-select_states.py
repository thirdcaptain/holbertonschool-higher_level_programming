#!/usr/bin/python3
"""Module lists all states from the database hbtn_0e_0_usa"""


if __name__=="__main__":
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="",
                         db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    for row in cur.fetchall():
        print(row)
    db.close()
