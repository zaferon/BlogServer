import sqlite3
import array

DB_PATH = '/home/base/myserver/articles.db'

def add_to_list(article):
    try:
        conn = sqlite3.connect(DB_PATH)

        # Once a connection has been established, use the cursor
        # object to execute queries
        c = conn.cursor()

        c.execute('insert into articles(title, identification, date, author, text) values(?,?,?,?,?,?)', (article['title'], article['identification'], article['date'], article['author'], article['text']))

        # Commit to save the change
        conn.commit()
        return {"title": article['title'], "identification": article['identification'], "date": article['date'], "author": article['author'], "text": article['text']}
    except Exception as e:
        print('Error: ', e)
        return None

def get_articles():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from articles')
        rows = c.fetchall()
        count = len(rows)
        articleList = [] * count
        x = 0
        while x < count:
            row = c.fetchone
            articleList.append(row)
        return { articleList}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_article(identification):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from articles where identification=?', (identification,))
        conn.commit()
        return {'identification': identification}
    except Exception as e:
        print('Error: ', e)
        return None
