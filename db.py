import pymysql

conn = pymysql.connect(host='localhost', user='root',
                       password='cldnjs2085!', db='wce', charset='utf8')

curs = conn.cursor()
query = 'desc info'
curs.execute(query)
