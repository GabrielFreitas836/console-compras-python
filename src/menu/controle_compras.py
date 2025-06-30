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
        "FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria ORDER BY p.idProduto;")
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

    # Função de inserção de dados na tabela 'pedidos' 
    #  Carregar os dados dos pedidos junto à outras colunas das outras tabelas
    def carregar_pedidos(self, idcliente):
        self.cliente = idcliente
        cursor = self.conn.cursor()

        # Buscando os IDs de itens para poder adiciona-los em 'pedidos' depois
        # ORDER BY utilizado para listar em ordem crescente e não causar problemas de pedidos sem clientes
        cursor.execute("SELECT idItens FROM itenspedidos ORDER BY idItens")
        self.rows = cursor.fetchall()
        for iditem in self.rows:
            pass
        cursor.execute("INSERT INTO pedidos (cliente_idCliente, item_idItem, pagamento_idPagamento) VALUES (%s, %s, 4);", (idcliente, iditem[0], ))
        self.conn.commit()

        cursor.execute("SELECT it.idItens, cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
        "FROM itenspedidos it " \
        "INNER JOIN pedidos p ON p.item_idItem = it.idItens " \
        "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
        "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
        "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria WHERE cl.idCliente = %s;", (idcliente,))

        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

    # Função de pagamento das compras
    def pagamento(self, idcliente):
        self.idcliente = idcliente
        cursor = self.conn.cursor()
        cursor.execute("SELECT cl.idCliente, cl.nome, SUM(it.valorTotal) AS totalComprado FROM pedidos p " \
        "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
        "INNER JOIN itenspedidos it ON p.item_idItem = it.idItens " \
        "WHERE cl.idCliente = %s;", (idcliente,))
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()

        for id, nome, total in self.rows:
            pass
        
        time.sleep(0.5)
        print("=" *50)
        print("Detalhes do pedido: \n")
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
        while True:
            try:
                print("\n[1] - Dinheiro\n[2] - Pix\n[3] - Cartão\n")
                forma_pagamento = int(input("Selecione a forma de pagamento: "))

                if forma_pagamento == 1:
                    print("Pagando em dinheiro...")
                    time.sleep(0.8)
                    print(f"R$ {total:.2f} pago com sucesso!")
                    self.atualizar_pagamento(forma_pagamento, idcliente)
                    break
                elif forma_pagamento == 2:
                    print("Pagando em pix...")
                    time.sleep(0.8)
                    print(f"R$ {total:.2f} pago com sucesso!")
                    self.atualizar_pagamento(forma_pagamento, idcliente)
                    break
                elif forma_pagamento == 3:
                    self.pagar_em_cartao(total)
                    self.atualizar_pagamento(forma_pagamento, idcliente)
                    break
                else:
                    print("Por favor, selecione [1] para dinheiro ou [2] para pix ou [3] para métodos de cartão")
                    continue
            except ValueError:
                print("Por favor, digite um valor válido!")

            
    
    # Função de controle de pagamento em cartão das compras
    def pagar_em_cartao(self, total):
        self.total = total

        while True:
            try:
                print("\n[1] - Débito\n[2] - Crédito\n")
                metodo = int(input("Escolha um dos métodos de pagamento: "))
            

                if metodo == 1:
                    print("Pagando com cartão no débito...")
                    time.sleep(0.8)
                    print(f"R$ {total:.2f} pago com sucesso!")
                    break
                elif metodo == 2:
                    print("\nNúmero de parcelas gerados: \n")
                    parcelas = []
                    if total < 10:
                        for i in range(1, 3):
                            n = i
                            m = total / n
                            info_parcelas = (n, m)
                            parcelas.append(info_parcelas)
                        
                        for (n, m) in parcelas:
                            print(f"{n} X R${m:.2f}")

                        print("\n")

                    elif 10 <= total < 30:
                        for i in range(1, 6):
                            n = i
                            m = total / n
                            info_parcelas = (n, m)
                            parcelas.append(info_parcelas)
                        
                        for (n, m) in parcelas:
                            print(f"{n} X R${m:.2f}")

                        print("\n")
                    
                    elif 30 <= total < 80:
                        for i in range(1, 9):
                            n = i
                            m = total / n
                            info_parcelas = (n, m)
                            parcelas.append(info_parcelas)
                        
                        for (n, m) in parcelas:
                            print(f"{n} X R${m:.2f}")

                        print("\n")

                    elif total >= 80:
                        for i in range(1, 13):
                            n = i
                            m = total / n
                            info_parcelas = (n, m)
                            parcelas.append(info_parcelas)
                        
                        for (n, m) in parcelas:
                            print(f"{n} X R${m:.2f}")

                        print("\n")
                    
                    escolha = int(input("Escolha o número de parcelas a ser pago: "))
                    for (n, m) in parcelas:
                        if escolha == n and escolha != 1:
                            print(f"Pagando {n} parcelas de R${m:.2f} ...")
                            time.sleep(0.5)
                            break
                        elif escolha == 1:
                            print(f"Pagando R${m:.2f} à vista no cartão...")
                            time.sleep(0.5)
                            break
                    break
                else:
                    print("Por favor, selecione [1] para débito ou [2] para parcelamento no crédito!")
                    continue
            except ValueError:
                print("Por favor, digite um valor válido!")

    # Função de atualizar a coluna de pagamento da tabela 'pedidos'
    def atualizar_pagamento(self, idpagamento, idcliente):
        self.idpagamento = idpagamento
        self.idcliente = idcliente
        cursor = self.conn.cursor()
        cursor.execute("UPDATE pedidos SET pagamento_idPagamento = %s WHERE cliente_idCliente = %s", (idpagamento, idcliente,))
        self.conn.commit()

    # Função de adicionar produtos ao 'itenspedidos'
    def adicionar_ao_carrinho(self, idcliente):
        print("\n")
        while True:

            valorTotal = 0.0

            try:
                escolhaProduto = int(input("Escolha qual produto quer comprar pelo ID: "))
                quantidadeProduto = int(input("Escolha a quantidade: "))

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

                    # Loop while utilizado para caso a opção seja inválida
                    while comprarDeNovo > 2:
                        print("Por favor, digite uma opção válida!")
                        print("\n[1] - Sim\n[2] - Não\n")
                        comprarDeNovo = int(input("Deseja comprar mais itens ? "))
                    else:  
                        if comprarDeNovo == 2:
                            self.pagamento(idcliente)
                            time.sleep(1)
                            break
                        elif comprarDeNovo == 1:
                            continue
            except ValueError:
                print("Por favor, digite um valor válido")
