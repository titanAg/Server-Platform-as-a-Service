# Kyle Orcutt

import os
import psycopg2
import datetime
from urllib import parse

DATABASE_URL = 'dbname=test host=localhost port=5432'

def app(environ, start_response):
    if environ['PATH_INFO'] == '/':
        with open('landing.html', 'r') as landing:
            html = landing.read()
            data = bytes(html, "utf-8")
            status = '200 OK'
        if environ['QUERY_STRING']:
            query = parse.parse_qs(environ['QUERY_STRING'])
            if 'url' in query.keys():
                url = query['url'][0]
                insert(url)
                data = bytes(url, "utf-8") # for testing
        query = """SELECT * FROM uptimedata"""
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        tabledata = ""
        for row in rows:
            url = "<td>" + row[0] + "</td>"
            status = "<td>" + row[1] + "</td>"
            code = "<td>" + str(row[2]) + "</td>"
            time = "<td>" + row[3].strftime("%m/%d/%Y, %H:%M:%S") + "</td>"
            tabledata += "<tr>" + url + status + code + time + "</tr>"
        data = bytes(html.replace("_data_", tabledata), "utf-8")
        cursor.close()
        conn.commit()
        conn.close()
        status = '200 OK'
    else:
        data = b'404 - Not Found Error'
        status = '404 Not Found'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(data))),
        ('COSC360', 'Kyle\'s server')
    ]
    start_response(status, response_headers)
    return iter([data])

def createTable():
    try:
        table = """
            CREATE TABLE uptimedata (
                url TEXT PRIMARY KEY,
                status TEXT,
                code INTEGER,
                last TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(table)
        cursor.close()
        conn.commit()
        conn.close()
        print("Created table.")
    except:
        print('Skipping table creation.')
        pass

def insert(url):
    try:
        statement = """INSERT INTO uptimedata (url, status, code, last)
                VALUES (%s, %s, %s, DEFAULT)"""
        status = "Unknown"
        code = 0
        vals = (url, "Unknown", 0)
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(statement, vals)
        cursor.close()
        conn.commit()
        conn.close()
        print("Inserted record.")
    except Exception as e:
        print("Failed to insert record.")
        print(e)
        pass

createTable()