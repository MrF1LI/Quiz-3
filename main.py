import requests
import sqlite3

url = "https://api.spaceflightnewsapi.net/v3/articles"
r = requests.get(url)
data = r.json()

# Connect to db

conn = sqlite3.connect("news.sqlite")
cursor = conn.cursor()


# Create table

cursor.execute('''CREATE TABLE IF NOT EXISTS news
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR (200),
                url VARCHAR (1000),
                newsSite VARCHAR (500),
                summary VARCHAR (2000));''')

# Save data

for news in data:
    news_data = (news["title"], news["url"], news["newsSite"], news["summary"])
    query = "INSERT INTO news (title, url, newsSite, summary) VALUES (?, ?, ?, ?)"
    cursor.execute(query, news_data)
    conn.commit()


conn.close()  # Disconnect
