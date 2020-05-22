import mysql.connector
con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    post="108.167.140.122",
    database="ardit700_pm1database"
)
cursor=con.cursor()
query=cursor.execute("SELECT*FROM Dictionary")
results=cursor.fetchall()

print(results)