# Kyle Orcutt

import os
import psycopg2
import urllib.request
from urllib.error import HTTPError, URLError

DATABASE_URL = 'dbname=test host=localhost port=5432'

def scheduled_job():
    print("I ran a scheduled job!")
    conn = psycopg2.connect(DATABASE_URL)
    query = """SELECT * FROM uptimedata"""
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        try:
            print("Trying url: " + row[0])
            response = urllib.request.urlopen(row[0])
            code = response.status
            status = "Site is up"
            update = """UPDATE uptimedata SET status=%s, code=%s, last=CURRENT_TIMESTAMP WHERE url=%s"""
            cursor.execute(update, (status, code, row[0]))
            conn.commit()
        except HTTPError as e:
            update = """UPDATE uptimedata SET status=%s, code=%s, last=CURRENT_TIMESTAMP WHERE url=%s"""
            cursor.execute(update, ("Site is unreachable", e.code, row[0]))
            conn.commit()
            pass
        except:
            update = """UPDATE uptimedata SET status=%s, code=%s, last=CURRENT_TIMESTAMP WHERE url=%s"""
            cursor.execute(update, ("Site is unreachable", 0, row[0]))
            conn.commit()
            pass
    cursor.close()
    conn.close()
    print('Finished website uptime checks!')

scheduled_job()