import csv
import sqlite3

conn = sqlite3.connect('E:\Django_Book_Projects\IOT\iot\db.sqlite3')
cursor = conn.cursor()
cursor.execute("select * from data_scan;")
print("Database created and Successfully Connected to SQLite")

with open("E:\Django_Book_Projects\IOT\iot\out.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()