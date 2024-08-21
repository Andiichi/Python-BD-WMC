# 8. Junção de Tabelas  
# Crie uma segunda tabela chamada "compras" com os campos: 
#           id (chave primária), 
#           cliente_id (chave estrangeira referenciando o id da tabela "clientes"), 
#           produto (texto) e 
#           valor (real). 
# 

import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'exercicios05_a_08\banco_loja.db')
cursor = conexao.cursor()


# Cria a tabela "clientes"
cursor.execute('''
CREATE TABLE compras (
    id INT PRIMARY KEY,
    produto VARCHAR(100),
    valor FLOAT,
    cliente_id INT,
    CONSTRAINT fk_clienteCompras FOREIGN KEY (cliente_id) REFERENCES clientes (id)
)
''')


# Insira algumas compras associadas a clientes existentes na tabela "clientes". 

# Insira alguns registros de compras na tabela.

# cursor.execute('''INSERT INTO clientes
#                 (id, nome, idade, saldo) 
#                 VALUES 
#                 (1, "Ana", 22, 2100.59)
# ''')

# cursor.execute('''INSERT INTO clientes
#                 (id, nome, idade, saldo) 
#                 VALUES 
#                 (2, "Giovanne", 30, 4100.59)
# ''')

# cursor.execute('''INSERT INTO clientes
#                 (id, nome, idade, saldo) 
#                 VALUES 
#                 (3, "Douglas", 20, 100.00)
# ''')


# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

#dados = cursor.execute('''
                # SELECT
                #     P.nome,
                #     P.preco,
                #     C.nome as Categoria
                # FROM
                #     produto P
                # INNER JOIN
                # categoria_produto C
                # ON P.id_categoria = C.id    
#               ''')

# dados = cursor.execute('''SELECT * 
#                           FROM clientes 
#                        ''') 

# for clientes in dados:
#     print(clientes)



# Confirma as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()