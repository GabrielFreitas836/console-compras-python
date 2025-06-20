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
        "FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria")
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

    # Função de adicionar produtos ao 'itenspedidos'
    def adicionar_ao_carrinho(self):
        print("\n")
        while True:
            valorTotal = 0.0

            try:
                escolhaProduto = int(input("Escolha qual produto quer comprar pelo ID: "))
                quantidadeProduto = int(input("Escolha a quantidade: "))
            except ValueError:
                print("Por favor, digite um valor válido")

            cursor = self.conn.cursor()
            cursor.execute("SELECT idProduto, valorUnitario FROM produtos")
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
                cursor.execute("INSERT INTO itenspedidos (quantidade, produto_idProduto, valorTotal) VALUES (%s, %s, %s)", (quantidadeProduto, escolhaProduto, valorTotal))
                self.conn.commit()
                print("Item salvo com sucesso!")
                time.sleep(0.3)
                print("=" *50)
                print("\n[1] - Sim\n [2] - Não")
                comprarDeNovo = int(input("Deseja comprar mais itens ? "))
                if comprarDeNovo == 2:
                    print("Sem problemas! Retornando ao início...")
                    time.sleep(1)
                    break
                elif comprarDeNovo == 1:
                    continue
