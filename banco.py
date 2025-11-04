import mysql.connector

# Conectar ao banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ano2021341",
    database="loja"
)
comando_sql = "DELETE FROM produtos WHERE id = %s"
cursor = conexao.cursor()

# Inserir novos clientes
sql = "INSERT INTO clientes (nome, idade) VALUES (%s, %s)"
valores = [
    ("João", 25),
    ("Maria", 30),
    ("Carlos", 22)
]
cursor.executemany(sql, valores)
conexao.commit()

# Mostrar todos os clientes
cursor.execute("SELECT * FROM clientes")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
#fechar conexão 
if 'conexao' in locals() and conexao.is_connected():
        cursor.close()  # <-- Fecha o mensageiro
        conexao.close() # <-- Fecha a porta do banco
        print("Conexão com o MySQL fechada.")