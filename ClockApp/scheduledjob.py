import os
import psycopg2
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
print("Hello World")

#@scheduler.scheduled_job('interval', minutes=5)
@scheduler.scheduled_job('cron', day_of_week='fri', hour=23, minute=59)
def scheduled_job():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    insert = "INSERT INTO logs VALUES (DEFAULT, 'I am scheduled job!', DEFAULT"
    cursor.execute(insert)
    conn.commit()
    conn.close()
    print('Finished timed job!')

scheduler.start()