# 4. Atualização e Remoção  

import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios01_a_04\banco_facul.db')
cursor = conexao.cursor()


#  UPDATE estudantes 
#  SET curso = 'Programação' 
#  WHERE id = 4;  



#    a) Atualize a idade de um aluno específico na tabela.  

# dados = cursor.execute('''
#                        UPDATE alunos 
#                        SET idade = 35
#                        WHERE id = 5
#                        ''') 


#    b) Remova um aluno pelo seu ID.

dados = cursor.execute('DELETE FROM alunos WHERE id = 2') 

dados = cursor.execute('SELECT * FROM alunos') 

for alunos in dados:
     print(alunos)




# Confirma as mudanças no banco de dados
conexao.commit()
print("\nDados inseridos com sucesso!")



# Fecha a conexão com o banco de dados
conexao.close()