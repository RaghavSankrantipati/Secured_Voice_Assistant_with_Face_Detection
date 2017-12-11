import pymysql

connection = pymysql.connect(host='ec2-184-72-98-174.compute-1.amazonaws.com', user='ralphie', password='buffalo', db='Book_A_MovieShow')
cursor = connection.cursor()
sql=("select * from Movie")
cursor.execute(sql)
data=cursor.fetchall()
print(data)