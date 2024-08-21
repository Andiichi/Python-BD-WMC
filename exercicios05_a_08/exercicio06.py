# 6. Consultas e Funções Agregadas  
#    Escreva consultas SQL para realizar as seguintes tarefas:  
#    a) Selecione nome e idade dos clientes com idade superior a 30 anos.  
#    b) Calcule o saldo médio dos clientes.  
#    c) Encontre o cliente com o saldo máximo.  
#    d) Conte quantos clientes têm saldo acima de 1000.

import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios05_a_08\banco_loja.db')
cursor = conexao.cursor()

#    a) Selecione nome e idade dos clientes com idade superior a 30 anos.  

# dados = cursor.execute('''SELECT nome, idade 
#                           FROM clientes 
#                           WHERE idade > 30
#                        ''') 

# for clientes in dados:
#     print(clientes)

#    b) Calcule o saldo médio dos clientes. 

# Executar a consulta SQL com o alias
# dados = cursor.execute("""
#                        SELECT AVG(saldo) AS 'Saldo médio' 
#                        FROM clientes
#                        """).fetchone() #exibir o valor de um alias específico, como Saldo médio com o fetchone()

# Exibir o resultado
# print(f"Saldo médio: {dados['Saldo médio']:.2f}")


#    c) Encontre o cliente com o saldo máximo. 

conexao.row_factory = sqlite3.Row  # Permite acessar os resultados como um dicionário
cursor = conexao.cursor()

# # Executar a consulta SQL com o alias
# dados = cursor.execute("""
#                        SELECT nome AS 'Nome', 
#                        MAX(saldo) AS 'Valor máximo' 
#                        FROM clientes
#                        """).fetchone() #exibir o valor de um alias específico, como Saldo médio com o fetchone()

# # Exibir o resultado
# print()
# print(f"Nome do cliente: {dados['Nome']}\nValor máximo: {dados['Valor máximo']:.2f}")


#    d) Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT count(*) AS "Total" FROM clientes WHERE saldo > 1000').fetchone()

print(f"Existe [{dados['Total']}] clientes com saldo acima de R$1000!")


# Confirma as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()