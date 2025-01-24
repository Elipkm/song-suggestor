import sqlite3

""" Execute to have a quick look at the database contents """

conn = sqlite3.connect("database/song_suggestor_demo.db")
result = conn.execute("select id, title, artist from song_data")

for row in result:
    print(row)

print("----")

result = conn.execute("select count(*) from song_keyword")
print("Number of keywords: ", result.fetchone()[0])
print("--> 9 keywords per song")
conn.close()