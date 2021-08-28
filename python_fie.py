import sqlite3
con = sqlite3.connect('movie_names.db')

cur = con.cursor()

cur.execute("INSERT INTO movies (movie_name, lead_actor, lead_actress, year_of_release, director_name) VALUES ('Titanic', 'Leonardo Dicaprio', 'Kate Winslet', 1997, 'James Cameron')")
con.commit()


for row in cur.execute('select * from movies'):
        print(row)

print ("\n")

cur.execute("select * from movies where lead_actor='Leonardo Dicaprio'")
print(cur.fetchall())

con.close()
