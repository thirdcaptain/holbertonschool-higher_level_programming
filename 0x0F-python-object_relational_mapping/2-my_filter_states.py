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

    # BINARY option makes query case sensitive
    SQLcommand = """SELECT * FROM states
                    WHERE BINARY states.name LIKE '{}'
                    ORDER BY states.id ASC""".format(argv[4])
    cur.execute(SQLcommand)

    for row in cur.fetchall():
        print(row)
    db.close()
