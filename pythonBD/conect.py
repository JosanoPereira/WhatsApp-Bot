import mysql.connector as mcon
from mysql.connector import errorcode

try:
    db_con = mcon.connect(host='localhost', user='root', password='josanojp25', database='bd')
    print('Conexão feita!')
except mcon.Error as erro:
    if erro.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe!')
    elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuário ou senha errada!')
    else:
        print(erro)
else:
    db_con.close()
