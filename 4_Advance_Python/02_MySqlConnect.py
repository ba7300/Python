#                                          Step-1 (Connection)

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300')
print(mydb)

if(mydb):
    print('Connection is successful')

else:
    print('Connection unsuccessful')
# X______________________X_________________________X____________________________X_____________________________X

#                                           Step-2 (Execution)


mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300')

mycursor=mydb.cursor()  
# cursor is an oject or variable in which all the databases / data are stored.
# It is a pointer to read perticular file or data from DB

# mycursor.execute("Create database <Database name eg.bhavikdb>")  
mycursor.execute("Show databases")

for i in mycursor:
    print(i)
# X______________________X_________________________X____________________________X_____________________________X

#                                            Step-3

mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300',database='bhavikdb')
mycursor=mydb.cursor()

#mycursor.execute("Create table employee(name varchar(200), sal int(20))")

mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)
# X______________________X_________________________X____________________________X_____________________________X

#                                            Step-4( Import in Db)

mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300',database='bhavikdb')
mycursor=mydb.cursor()


sqlform='Insert into employee(name,sal) values(%s,%s)'
employees=[("Dhiru",25000),("Viky",10000),("Janmesh",15000), ]


mycursor.executemany(sqlform,employees)
mydb.commit()
# X______________________X_________________________X____________________________X_____________________________X

#                                            Step-5 (Fetch Data from Db)


mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300',database='bhavikdb')
mycursor=mydb.cursor()

#mycursor.execute('Select name from employee')
mycursor.execute("Select * from employee")


#myresult=mycursor.fetchone()
myresult=mycursor.fetchall()

for row in myresult:
    print(row) 
# X______________________X_________________________X____________________________X_____________________________X


#                                            Step-6 (Update Db)


mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300',database='bhavikdb')
mycursor=mydb.cursor()

sql="UPDATE employee SET sal=20000 where name='Dhiru'"
mycursor.execute(sql)

mydb.commit()
# X______________________X_________________________X____________________________X_____________________________X


#                                             Step-7 (Delete Db)


mydb=mysql.connector.connect(host='localhost',user='root',passwd='ba7300',database='bhavikdb')
mycursor=mydb.cursor()

sql="DELETE FROM employee WHERE name='Viky'"
mycursor.execute(sql)

mydb.commit()