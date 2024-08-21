# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios01_a_04\banco_facul.db')

cursor = conexao.cursor()

cursor.execute('''INSERT INTO alunos
                (id, nome, idade, curso) 
                VALUES 
                (1, "Ana", 22, "Engenharia")
''')

cursor.execute('''INSERT INTO alunos
                (id, nome, idade, curso) 
                VALUES 
                (2, "Bruna", 29, "Química")
''')

cursor.execute('''INSERT INTO alunos
                (id, nome, idade, curso) 
                VALUES 
                (3, "Beatriz", 18, "Marketing Digital")
''')

cursor.execute('''INSERT INTO alunos
                (id, nome, idade, curso) 
                VALUES 
                (4, "Pedro", 22, "Engenharia")
''')

cursor.execute('''INSERT INTO alunos
                (id, nome, idade, curso) 
                VALUES 
                (5, "Leonardo", 40, "TI")
''')



# Confirma as mudanças no banco de dados
conexao.commit()
print("Dados inseridos com sucesso!")



# Fecha a conexão com o banco de dados
conexao.close()
