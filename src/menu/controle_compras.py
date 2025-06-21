"""
    arquivo: controle_compras.py
    autor: Gabriel da Silva Freitas
    data: 20/06/2025
    descricao: controle das compras realizadas pelos clientes
"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
import time

class Compras(ConectarBanco):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    # Função de carregar os dados da tabela 'produtos' + 'categorias'
    def carregar_produtos(self):
        time.sleep(0.2)
        print("=" *50)
        print("\n")
        cursor = self.conn.cursor()
        cursor.execute("SELECT p.idProduto, p.descricao AS produto, p.valorUnitario, c.descricao AS categoria " \
        "FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria;")
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

    # Função de inserção de dados na tabela 'pedidos' 
    #  Carregar os dados dos pedidos junto à outras colunas das outras tabelas
    def carregar_pedidos(self, idcliente):
        self.cliente = idcliente
        cursor = self.conn.cursor()

        # Buscando os IDs de itens para poder adiciona-los em 'pedidos' depois
        #ORDER BY utilizado para listar em ordem crescente e não causar problemas de pedidos sem clientes
        cursor.execute("SELECT idItens FROM itenspedidos ORDER BY idItens")
        itens = cursor.fetchall()
        for iditem in itens:
            pass
        cursor.execute("INSERT INTO pedidos (cliente_idCliente, item_idItem, pagamento_idPagamento) VALUES (%s, %s, 4);", (idcliente, iditem[0], ))
        self.conn.commit()

        cursor.execute("SELECT cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
        "FROM itenspedidos it " \
        "INNER JOIN pedidos p ON p.item_idItem = it.idItens " \
        "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
        "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
        "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria;")

        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

    def pagamento(self, valorTotal):
        self.valorTotal = valorTotal
        print("Valor total: ", self.valorTotal)
        
    # Função de adicionar produtos ao 'itenspedidos'
    def adicionar_ao_carrinho(self, idcliente):
        print("\n")
        while True:

            valorTotal = 0.0

            try:
                escolhaProduto = int(input("Escolha qual produto quer comprar pelo ID: "))
                quantidadeProduto = int(input("Escolha a quantidade: "))
            except ValueError:
                print("Por favor, digite um valor válido")

            cursor = self.conn.cursor()
            cursor.execute("SELECT idProduto, valorUnitario FROM produtos;")
            self.rows = cursor.fetchall()
            
            for id, valor in self.rows:
                if id == escolhaProduto:
                    valorTotal = valor * quantidadeProduto
                    escolhaProduto = id
                    break
            
            if escolhaProduto != id:
                print("ID Inválido! Tente novamente!")
                time.sleep(1)
                continue
            else:
                cursor.execute("INSERT INTO itenspedidos (quantidade, produto_idProduto, valorTotal) VALUES (%s, %s, %s)", (quantidadeProduto, escolhaProduto, valorTotal,))
                self.conn.commit()
                print("Item salvo com sucesso!")
                time.sleep(0.3)
                print("=" *50)

                self.carregar_pedidos(idcliente)

                print("\n[1] - Sim\n[2] - Não\n")
                comprarDeNovo = int(input("Deseja comprar mais itens ? "))
                if comprarDeNovo == 2:
                    self.pagamento(valorTotal)
                    time.sleep(1)
                    break
                elif comprarDeNovo == 1:
                    continue
