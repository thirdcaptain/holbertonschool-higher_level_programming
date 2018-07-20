#!/usr/bin/python3
"""Module lists all states that match name argument"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # default values user="root", passwd="", db="hbtn_0e_0_usa"
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()

    # %s placeholder fills values more safely
    state_lookup = str(argv[4])
    SQLcommand = """SELECT * FROM states
                    WHERE states.name=%s
                    ORDER BY states.id ASC"""
    cur.execute(SQLcommand, (state_lookup,))

    for row in cur.fetchall():
        print(row)
    db.close()
