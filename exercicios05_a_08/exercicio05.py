# 5. Criar uma Tabela e Inserir Dados  
#    Crie uma tabela chamada "clientes" com os campos: 
#       id (chave primária), 
#       nome (texto), 
#       idade (inteiro) e 
#       saldo (float). 
# 


import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios05_a_08\banco_loja.db')
cursor = conexao.cursor()

# Cria a tabela "clientes"
# cursor.execute('''
# CREATE TABLE clientes (
#     id INT PRIMARY KEY,
#     nome VARCHAR(100),
#     idade INT,
#     saldo FLOAT
# )
# ''')



# Insira alguns registros de clientes na tabela.

# cursor.execute('''INSERT INTO clientes
#                 (id, nome, idade, saldo) 
#                 VALUES 
#                 (1, "Ana", 22, 2100.59)
# ''')

cursor.execute('''INSERT INTO clientes
                (id, nome, idade, saldo) 
                VALUES 
                (2, "Giovanne", 30, 4100.59)
''')

cursor.execute('''INSERT INTO clientes
                (id, nome, idade, saldo) 
                VALUES 
                (3, "Douglas", 20, 100.00)
''')

cursor.execute('''INSERT INTO clientes
                (id, nome, idade, saldo) 
                VALUES 
                (4, "Analise", 52, 22100.59)
''')

cursor.execute('''INSERT INTO clientes
                (id, nome, idade, saldo) 
                VALUES 
                (5, "Fernando", 62, 2300.59)
''')


# Confirma as mudanças no banco de dados
conexao.commit()

print('Banco de dados atualizado com sucesso!')

# Fecha a conexão com o banco de dados
conexao.close()