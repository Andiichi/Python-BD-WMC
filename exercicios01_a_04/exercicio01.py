# 1. Crie uma tabela chamada "alunos" com os seguintes campos: 
#       id (inteiro), 
#       nome (texto), 
#       idade (inteiro) e 
#       curso (texto).

import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios01_a_04\banco_facul.db')
cursor = conexao.cursor()

# Cria a tabela "alunos"
cursor.execute('''
CREATE TABLE alunos (
    id INT,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(100)
)
''')

# Confirma as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()

print("Tabela 'alunos' criada com sucesso!")