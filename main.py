import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bemvindo@digital",
    database="bdyoutube",
)
cursor = conexao.cursor()
nome_produto = "todynho"
comando = f'DELETE FROM vendinhas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()

#CREATE
#nome_produto = "chocolate"
#valor = 27
#comando = f'INSERT INTO vendinhas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
#cursor.execute(comando)
#conexao.commit()

#READ
#comando = f'SELECT * FROM vendinhas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPDATE
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendinhas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

#DELETE
#nome_produto = "todynho"
#comando = f'DELETE FROM vendinhas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

