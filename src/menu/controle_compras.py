"""
    arquivo: controle_compras.py
    autor: Gabriel da Silva Freitas
    data: 20/06/2025
    descricao: controle das compras realizadas pelos clientes
"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
# Biblioteca utilizada para colorir textos
from colorama import Fore, Style
import time

class Compras(ConectarBanco):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    # Função de carregar os dados da tabela 'produtos' + 'categorias'
    def carregar_produtos(self, categoriaEscolhida):
        while True:
            try:
                time.sleep(0.2)
                print("=" *50)
                print("\n[1] - Higiene\n[2] - Limpeza\n[3] - Hortifruti\n[4] - Açougue\n[5] - Doces\n[6] - Festa\n")
                categoriaEscolhida = int(input("Escolha uma categoria: "))
                # Lógica de separação por categorias
                cursor = self.conn.cursor()
                cursor.execute("""SELECT p.idProduto, p.descricao AS produto, p.valorUnitario
                FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria WHERE c.idCategoria = %s ORDER BY p.idProduto;""", (categoriaEscolhida,))
                self.columms = [desc[0] for desc in cursor.description]
                self.rows = cursor.fetchall()
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                print("\n[1] - Sim\n[2] - Não\n")
                trocarCategoria = int(input("Deseja ver outra categoria ? "))
                if trocarCategoria == 1:
                    continue
                elif trocarCategoria == 2:
                    return categoriaEscolhida
                else:
                    print("Opção inválida! Tente novamente!")
                    continue
            except ValueError:
                print("Por favor, digite um valor válido!")
                continue

    # Função de inserção de dados na tabela 'pedidos' 
    #  Carregar os dados dos pedidos junto à outras colunas das outras tabelas
    def carregar_pedidos(self, idcliente):
        self.cliente = idcliente
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO pedidos (cliente_idCliente, pagamento_idPagamento) VALUES (%s, 4);", (idcliente,))
        self.conn.commit()

    # Função de pagamento das compras
    def pagamento(self, idcliente):
        self.idcliente = idcliente
        cursor = self.conn.cursor()
        cursor.execute("SELECT cl.idCliente, cl.nome, SUM(it.valorTotal) AS totalComprado FROM pedidos p " \
        "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
        "INNER JOIN itenspedidos it ON p.idPedido = it.pedido_idPedido " \
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

    # Função de remover um item do carrinho
    def remover_item(self, idcliente):
        while True:
            cursor = self.conn.cursor()
            cursor.execute("SELECT it.idItens, cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
            "FROM itenspedidos it " \
            "INNER JOIN pedidos p ON p.idPedido = it.pedido_idPedido " \
            "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
            "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
            "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria WHERE cl.idCliente = %s;", (idcliente,))

            self.columms = [desc[0] for desc in cursor.description]
            self.rows = cursor.fetchall()

            if self.rows == []:
                print("Não há itens registrados!")
                return False
            elif len(self.rows) == 1:
                print("Não é possível remover um item do carrinho quando só há uma linha registrada!")
                time.sleep(0.3)
                return False
            else:
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                itemRemovido = int(input("Escolha qual item será removido pelo ID: "))

                for id, cliente, produto, valorUni, categoria, quantidade, valorTot in self.rows:
                    if id == itemRemovido:
                        cursor = self.conn.cursor()
                        cursor.execute("DELETE FROM itenspedidos WHERE idItens = %s;", (itemRemovido,))
                        self.conn.commit()
                        id = itemRemovido
                        print("Item removido com sucesso!")
                        if len(self.rows) > 1:
                            return True
                        break
                
                if id != itemRemovido:
                    print("Item não encontrado! Tente novamente!")
                    continue
                else:
                    break
    
    # Função de diminuir a quantidade de um item do carrinho
    # Essa função considera todas as possibilidades de efeito pós-deleção
    def diminuir_quantidade(self, idcliente, valorTotal):
        while True:
            try:
                print("=" *50)
                cursor = self.conn.cursor()
                cursor.execute("SELECT it.idItens, cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
                "FROM itenspedidos it " \
                "INNER JOIN pedidos p ON p.idPedido = it.pedido_idPedido " \
                "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
                "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
                "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria WHERE cl.idCliente = %s ORDER BY it.idItens;", (idcliente,))

                self.columms = [desc[0] for desc in cursor.description]
                self.rows = cursor.fetchall()
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                print("\n")
                diminuir = int(input("Escolha qual produto você quer diminuir a quantidade pelo ID do item: "))
                qtdDiminuida = int(input("Escolha a quantidade que quer diminuir: "))

                for item, cliente, produto, valorUni, categoria, quantidade, valorTot in self.rows:
                    if item == diminuir:
                        cursor.execute("""SELECT it.quantidade FROM itenspedidos it INNER JOIN pedidos p
                        ON it.pedido_idPedido = p.idPedido WHERE p.cliente_idCliente = %s AND it.idItens = %s;""", (idcliente, diminuir,))
                        qtdProduto = cursor.fetchone()
                        if qtdDiminuida < qtdProduto[0]:
                            qtdMenos = qtdProduto[0] - qtdDiminuida
                            valorTotal = qtdMenos * valorUni
                            cursor.execute("UPDATE itenspedidos SET valorTotal = %s, quantidade = %s WHERE idItens = %s;", (valorTotal, qtdMenos, diminuir,))
                            self.conn.commit()
                            print("Item atualizado com sucesso!")
                            return valorTotal, True
                        elif qtdDiminuida == qtdProduto[0]:
                            print(f"Já que você quer diminuir {qtdDiminuida} de {qtdProduto[0]} desse produto, seu item será removido!")
                            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                            cursor.execute("DELETE p FROM pedidos p INNER JOIN itenspedidos it ON it.pedido_idPedido = p.idPedido WHERE it.idItens = %s;", (diminuir,))
                            cursor.execute("DELETE FROM itenspedidos WHERE idItens = %s;", (diminuir,))
                            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                            self.conn.commit()
                            time.sleep(0.2)
                            print("Item removido com sucesso!")

                            cursor.execute("SELECT it.idItens, cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
                            "FROM itenspedidos it " \
                            "INNER JOIN pedidos p ON p.idPedido = it.pedido_idPedido " \
                            "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
                            "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
                            "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria WHERE cl.idCliente = %s ORDER BY it.idItens;", (idcliente,))
                            self.rows = cursor.fetchall()

                            if self.rows == []:
                                print("Seu carrinho está vazio agora! Cancelando sua compra...")
                                time.sleep(0.5)
                                print("Desativando restrições de chaves estrangeiras temporariamente...")
                                time.sleep(1.3)
                                cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                                print("Removendo pedido e itens...")
                                time.sleep(1.3)
                                cursor.execute("DELETE it FROM itenspedidos it INNER JOIN pedidos p ON it.pedido_idPedido = p.idPedido WHERE p.cliente_idCliente = %s;", (idcliente,))
                                cursor.execute("DELETE FROM pedidos WHERE cliente_idCliente = %s;", (idcliente,))
                                print("Compra cancelada!")
                                time.sleep(0.3)
                                print("Reativando restrições de chaves estrangeiras...")
                                cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                                self.conn.commit()
                                time.sleep(0.3)
                                print("Retornando ao início...")
                            return True
                        elif qtdDiminuida > qtdProduto[0]:
                            print("Não é possível diminuir uma quantidade maior do que a quantidade comprada! Tente novamente!")
                            return False
                if item != diminuir:
                    print("Esse ID não corresponde a algum dos itens registrados no carrinho atualmente! Tente novamente!")
                    continue
                if True:
                    break
            except ValueError:
                print("Por favor, digite um valor válido!")

    # Função de cancelar a compra
    def cancelar_compra(self, idcliente):
        try:
            time.sleep(1)
            print("=" *50)
            print("\n[1] - Sim\n[2] - Não\n")
            cancelar = int(input("Você realmente deseja cancelar a compra ? "))
            if cancelar == 2:
                return False
            elif cancelar == 1:
                cursor = self.conn.cursor()
                print("Desativando restrições de chaves estrangeiras temporariamente...")
                time.sleep(1.3)
                cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                print("Removendo pedido e itens...")
                time.sleep(1.3)
                cursor.execute("DELETE it FROM itenspedidos it INNER JOIN pedidos p ON it.pedido_idPedido = p.idPedido WHERE p.cliente_idCliente = %s;", (idcliente,))
                cursor.execute("DELETE FROM pedidos WHERE cliente_idCliente = %s;", (idcliente,))
                print("Compra cancelada!")
                time.sleep(0.3)
                print("Reativando restrições de chaves estrangeiras...")
                cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                self.conn.commit()
                time.sleep(0.3)
                print("Retornando ao início...")
                return True
        except ValueError:
            print("Por favor, digite um valor válido!")


    # Função de adicionar produtos ao 'itenspedidos'
    def adicionar_ao_carrinho(self, idcliente):
        print("\n")
        categoriaEscolhida = 0
        valorTotal = 0.0
        qtdExtra = 0
        remover = False

        while True:
            try:
                produtos = self.carregar_produtos(categoriaEscolhida)
                categoriaEscolhida = produtos

                trigger1 = True
                trigger2 = True

                escolhaProduto = int(input("Escolha qual produto quer comprar pelo ID: "))
                quantidadeProduto = int(input("Escolha a quantidade: "))
                
                # Procura no banco os produtos da categoria escolhida
                # Se o ID do produto digitado não corresponder à categoria escolhida, ele não adicionará o item ao carrinho
                cursor = self.conn.cursor()
                cursor.execute("""SELECT p.idProduto, p.descricao AS produto FROM produtos p 
                JOIN categorias c ON p.categoria_idCategoria = c.idCategoria WHERE c.idCategoria = %s ORDER BY p.idProduto;""", (categoriaEscolhida,))
                self.rows = cursor.fetchall()

                for id, produto in self.rows:
                    if id == escolhaProduto:
                        escolhaProduto = id
                        break

                if escolhaProduto != id:
                    print("Esse ID não pertence à categoria escolhida!")
                    time.sleep(0.3)
                    print("Tente novamente!")
                    continue
                else:                    
                    # Selecionando a quantidade de um item a partir do cliente atual e do produto escolhido atual
                    cursor = self.conn.cursor()
                    cursor.execute("""SELECT it.quantidade FROM itenspedidos it INNER JOIN pedidos p
                    ON it.pedido_idPedido = p.idPedido WHERE p.cliente_idCliente = %s AND it.produto_idProduto = %s;""", (idcliente, escolhaProduto, ))
                    qtdProduto = cursor.fetchone()
                    if qtdProduto == None:
                        qtdProduto = 0
                        qtdExtra = qtdProduto + quantidadeProduto
                    else:
                        qtdExtra = qtdProduto[0] + quantidadeProduto

                    cursor.execute("SELECT idProduto, valorUnitario FROM produtos;")
                    self.rows = cursor.fetchall()
                    
                    for id, valor in self.rows:
                        if id == escolhaProduto:
                            valorTotal = valor * qtdExtra
                            escolhaProduto = id
                            break
                    
                    if escolhaProduto != id:
                        print("ID Inválido! Tente novamente!")
                        time.sleep(1)
                        continue
                    else:
                        self.carregar_pedidos(idcliente)

                        cursor.execute("SELECT idPedido FROM pedidos WHERE cliente_idCliente = %s;", (idcliente,))
                        self.rows = cursor.fetchall()

                        for idpedido in self.rows:
                            pass

                        cursor.execute("SELECT p.cliente_idCliente, it.produto_idProduto, COUNT(produto_idProduto) AS total FROM itenspedidos it INNER JOIN pedidos p ON p.idPedido = it.pedido_idPedido INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto WHERE p.cliente_idCliente = %s AND it.produto_idProduto = %s AND pr.categoria_idCategoria = %s GROUP BY p.cliente_idCliente, it.produto_idProduto ORDER BY p.cliente_idCliente, it.produto_idProduto;", (idcliente, escolhaProduto, categoriaEscolhida,))
                        self.rows = cursor.fetchall()

                        if self.rows == []:
                            cursor.execute("INSERT INTO itenspedidos (quantidade, pedido_idPedido, produto_idProduto, valorTotal) VALUES (%s, %s, %s, %s)", (qtdExtra, idpedido[0], escolhaProduto, valorTotal,))
                            self.conn.commit()
                            print("Item salvo com sucesso!")
                            time.sleep(0.3)
                            print("=" *50)
                        else:
                            for cliente, produto, total in self.rows:
                                if total >= 1 and produto == escolhaProduto:
                                    cursor.execute("UPDATE itenspedidos SET quantidade = %s, valorTotal = %s WHERE produto_idProduto = %s;", (qtdExtra, valorTotal, escolhaProduto,))
                                    self.conn.commit()
                                    print("Item atualizado com sucesso!")
                                    time.sleep(0.3)
                                    print("=" *50)
                                elif total >= 1 and produto != escolhaProduto:
                                    cursor.execute("INSERT INTO itenspedidos (quantidade, pedido_idPedido, produto_idProduto, valorTotal) VALUES (%s, %s, %s, %s)", (qtdExtra, idpedido[0], escolhaProduto, valorTotal,))
                                    cursor.execute("UPDATE itenspedidos SET quantidade = %s, valorTotal = %s WHERE produto_idProduto = %s;", (qtdExtra, valorTotal, escolhaProduto,))
                                    self.conn.commit()
                                    print("Item salvo e atualizado com sucesso!")
                                    time.sleep(0.3)
                                    print("=" *50)
                        while trigger1:
                            cursor.execute("SELECT it.idItens, cl.nome AS cliente, pr.descricao AS produto, pr.valorUnitario, ca.descricao AS categoria, it.quantidade, it.valorTotal " \
                            "FROM itenspedidos it " \
                            "INNER JOIN pedidos p ON p.idPedido = it.pedido_idPedido " \
                            "INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
                            "INNER JOIN produtos pr ON pr.idProduto = it.produto_idProduto " \
                            "INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria WHERE cl.idCliente = %s ORDER BY it.idItens;", (idcliente,))

                            self.columms = [desc[0] for desc in cursor.description]
                            self.rows = cursor.fetchall()
                            
                            if len(self.rows) > 1:
                                remover = True
                            else:
                                remover = False

                            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

                            if remover:
                                print("\n[1] - Comprar mais itens\n[2] - Encerrar as compras\n[3] - Remover um item do carrinho\n[4] - Diminuir quantidade de um produto\n[5] - Cancelar compra\n")
                            elif not remover:
                                print("\n[1] - Comprar mais itens\n[2] - Encerrar as compras", Fore.BLACK + "\n[3] - Remover um item do carrinho", Style.RESET_ALL + "\n[4] - Diminuir quantidade de um produto\n[5] - Cancelar compra\n")

                            opcoes = int(input("O que deseja fazer agora ? "))

                            # Loop while utilizado para caso a opção seja inválida
                            while opcoes > 5:
                                print("Por favor, digite uma opção válida!")
                                if remover:
                                    print("\n[1] - Comprar mais itens\n[2] - Encerrar as compras\n[3] - Remover um item do carrinho\n[4] - Diminuir quantidade de um produto\n[5] - Cancelar compra\n")
                                elif not remover:
                                    print("\n[1] - Comprar mais itens\n[2] - Encerrar as compras", Fore.BLACK + "\n[3] - Remover um item do carrinho", Style.RESET_ALL + "\n[4] - Diminuir quantidade de um produto\n[5] - Cancelar compra\n")

                                opcoes = int(input("O que deseja fazer agora ? "))
                            else:  
                                if opcoes == 2:
                                    trigger1 = False
                                    self.pagamento(idcliente)
                                    cursor.close()
                                    trigger2 = False
                                    time.sleep(1)
                                elif opcoes == 1:
                                    trigger1 = False
                                    continue
                                elif opcoes == 3:
                                    trigger1 = True
                                    remover = self.remover_item(idcliente)
                                    continue
                                elif opcoes == 4:
                                    diminuir = self.diminuir_quantidade(idcliente, valorTotal)
                                    if diminuir and self.rows == []:
                                        trigger1 = False
                                        trigger2 = False
                                    elif diminuir and self.rows != []:
                                        trigger1 = True
                                        continue
                                elif opcoes == 5:
                                    cancelar = self.cancelar_compra(idcliente)
                                    if cancelar:
                                        trigger1 = False
                                        trigger2 = False
                                        cursor.close()
                                        time.sleep(1)
                                    elif not cancelar:
                                        trigger1 = True
                                        continue
                    if not trigger2:
                        break
            except ValueError:
                print("Por favor, digite um valor válido")
                continue
