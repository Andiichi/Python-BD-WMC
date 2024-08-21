# 7. Atualização e Remoção com Condições  
#    a) Atualize o saldo de um cliente específico.  
#    b) Remova um cliente pelo seu ID.


import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios05_a_08\banco_loja.db')
# conexao.row_factory = sqlite3.Row  # Permite acessar os resultados como um dicionário
cursor = conexao.cursor()

#    a) Atualize o saldo de um cliente específico.  

# dados = cursor.execute('''UPDATE clientes 
#                           SET saldo = 450
#                           WHERE id = 5
#                        ''') 


# dados = cursor.execute('''SELECT * 
#                           FROM clientes 
#                        ''') 

# for clientes in dados:
#     print(clientes)


#    b) Remova um cliente pelo seu ID.


dados = cursor.execute('''DELETE FROM clientes 
                       WHERE ID = 3
                       ''') 

dados = cursor.execute('''SELECT * 
                          FROM clientes 
                       ''') 

for clientes in dados:
    print(clientes)




# Confirma as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()