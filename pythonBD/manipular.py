from datetime import date
import mysql.connector as mcon

db_con = mcon.connect(
    host='localhost', 
    user='root', 
    password='josanojp25', 
    database='bd'
)

cursor = db_con.cursor()

'''
for i in range(5):
    nome = input('Insira o nome:')
    bi = input('Insira o BI: ')
    sql = "INSERT INTO usuario(nome, bi) VALUES(%s, %s)"
    values = (nome, bi)
    cursor.execute(sql, values)
'''

sql = "update usuario set nome =%s where id=%s"
up = ('Pereira', 3)
cursor.execute(sql, up)

cursor.close()
db_con.commit()
db_con.close()

