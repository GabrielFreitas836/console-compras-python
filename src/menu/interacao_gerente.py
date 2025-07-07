"""
    arquivo: interacao_gerente.py
    autor: Gabriel Freitas
    data: 16/06/2025
    descricao: interações relacionadas ao gerente na aplicação console
"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
# Biblioteca utilizada para colorir textos
from colorama import Fore, Style 
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Gerente(ConectarBanco):
    def __init__(self, conn = None):
        super().__init__()
        self.conn = conn

    # Função principal que gerencia as opções do gerente
    def opcoes_gerente(self):
        while True:
            print("\n[1] - Clientes\n[2] - Produtos\n[3] - Itens e Pedidos\n")
            escolha = int(input("Em qual categoria gostaria de mexer ? "))

            match escolha:
                case 1:
                    print("Abrindo aba de clientes...")
                    time.sleep(1)
                    print("=" *50)
                    verificado = self.verificar_tabelas("clientes")
                    if verificado:
                        print("\n[1] - Adicionar um novo cliente\n[2] - Alterar dados de um cliente existente\n[3] - Deletar um cliente existente\n[4] - Mostrar tabela de clientes\n[5] - Limpar tabela de clientes\n")
                    else:
                        print("\n[1] - Adicionar um novo cliente", Fore.BLACK + "\n[2] - Alterar dados de um cliente existente" + Style.RESET_ALL, Fore.BLACK + "\n[3] - Deletar um cliente existente" + Style.RESET_ALL, "\n[4] - Mostrar tabela de clientes\n[5] - Limpar tabela de clientes\n")

                    subescolha = int(input("O que você gostaria de fazer ? "))

                    if subescolha == 1:
                        self.adicionar_cliente()
                        break
                    elif subescolha == 2:
                        self.atualizar_cliente()
                        break
                    elif subescolha == 3:
                        self.deletar_cliente()
                        break
                    elif subescolha == 4:
                        time.sleep(1)
                        print("\n")
                        cursor = self.conn.cursor()
                        cursor.execute("SELECT idCliente, nome, idade FROM clientes;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()

                        if self.rows == []:
                            print("Não há clientes registrados!")
                            continue
                        else:
                            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                            break

                    elif subescolha == 5:
                        self.limpar_clientes()
                        break
                    else:
                        print("Opção inválida! Retornando ao início...")
                        time.sleep(0.5)
                        continue
                case 2:
                    print("Abrindo aba de produtos...")
                    time.sleep(1)
                    print("=" *50)
                    verificado = self.verificar_tabelas("produtos")
                    if verificado:
                        print("\n[1] - Adicionar um novo produto\n[2] - Alterar dados de um produto existente\n[3] - Deletar um produto existente\n[4] - Mostrar tabela de produtos\n[5] - Limpar tabela de produtos\n")
                    else:
                        print("\n[1] - Adicionar um novo produto", Fore.BLACK + "\n[2] - Alterar dados de um produto existente" + Style.RESET_ALL, Fore.BLACK + "\n[3] - Deletar um produto existente" + Style.RESET_ALL, "\n[4] - Mostrar tabela de produtos\n[5] - Limpar tabela de produtos\n")

                    subescolha = int(input("O que você gostaria de fazer ? "))

                    if subescolha == 1:
                        self.adicionar_produto()
                        break
                    elif subescolha == 2:
                        self.atualizar_produtos()
                        break
                    elif subescolha == 3:
                        self.deletar_produto()
                        break
                    elif subescolha == 4:
                        time.sleep(1)
                        print("\n")
                        cursor = self.conn.cursor()
                        cursor.execute("SELECT p.idProduto, p.descricao AS produto, p.valorUnitario, c.descricao AS categoria " \
                        "FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()

                        if self.rows == []:
                            print("Não há produtos registrados!")
                            continue
                        else:
                            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                            break
                    elif subescolha == 5:
                        self.limpar_produtos()
                        break
                    else:
                        print("Opção inválida! Retornando ao início...")
                        time.sleep(0.5)
                        continue
                case 3:
                    print("Abrindo aba de pedidos...")
                    time.sleep(1)
                    print("=" *50)
                    print("\n[1] - Mostrar tabela de pedidos\n[2] - Deletar pedido existente\n[3] - Limpar tabela de pedidos\n")
                    subescolha = int(input("O que você gostaria de fazer ? "))

                    if subescolha == 1:
                        time.sleep(1)
                        print("\n")
                        cursor = self.conn.cursor()
                        cursor.execute("SELECT p.idPedido, cl.nome AS cliente, it.quantidade, pr.descricao AS produto, pr.valorUnitario, it.valorTotal, pa.descricao AS formaPagamento FROM pedidos p INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
                        "INNER JOIN itenspedidos it ON it.pedido_idPedido = p.idPedido " \
                        "INNER JOIN produtos pr ON it.produto_idProduto = pr.idProduto " \
                        "INNER JOIN pagamento pa ON p.pagamento_idPagamento = pa.idPagamento ORDER BY p.idPedido;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()

                        if self.rows == []:
                            print("Não há pedidos registrados!")
                            continue
                        else:
                            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                            break
                    elif subescolha == 2:
                        self.deletar_pedido()
                        continue
                    
                    elif subescolha == 3:
                        self.limpar_pedidos()
                        break

                    else:
                        print("Opção inválida! Retornando ao início...")
                        time.sleep(0.5)
                        continue

                case _:
                    print("=" *50, "\n")
                    print("Escolha uma das opções disponíveis: ")
                    continue
    
    # Função de verificar a existência de valores numa tabela
    # O nome da tabela deve ser passado como parâmetro e só será aceito os nomes da lista
    def verificar_tabelas(self, tabela):
        self.tabela = tabela
        cursor = self.conn.cursor()
        # Evitar SQL Injection
        tabelas_permitidas = ["clientes", "produtos", "pedidos", "itenspedidos"]
        if tabela in tabelas_permitidas:
            cursor.execute(f"SELECT * FROM {tabela};")
            self.rows = cursor.fetchall()
        else:
            raise ValueError("Nome de tabela não permitido!")

        if self.rows == []:
            return False
        else:
            return True
    
    # Função de adicionar um novo cliente
    def adicionar_cliente(self):
        while True:
            try:
                nome = input("Digite o nome do cliente: ")
                idade = int(input("Digite a idade do cliente: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s);", (nome, idade,))
                self.conn.commit()
                time.sleep(1)
                print(f"Cliente {nome} adicionado(a) com sucesso!")
                time.sleep(0.7)
                print("\n[1] - Sim\n[2] - Não\n")
                escolha = int(input("Deseja adicionar mais ? "))

                if escolha == 1:
                    continue
                elif escolha == 2:
                    cursor.close()
                    break
                else:
                    print("Opção inválida! Tente novamente!")
                    continue
            except ValueError:
                print("Por favor, digite um valor válido!")
            

    # Função de adicionar um novo produto
    def adicionar_produto(self):
        while True:
            try:
                produto = input("Qual será o produto ? ").upper()
                valorUnitario = float(input("Qual será o valor unitário do produto ? "))
                
                cursor = self.conn.cursor()
                cursor.execute("SELECT idCategoria, descricao FROM categorias;")
                self.columms = [desc[0] for desc in cursor.description]
                self.rows = cursor.fetchall()
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                print("\n")

                categoria = int(input("Escolha a categoria do produto a partir de seu ID: "))
                cursor.execute("INSERT INTO produtos (descricao, valorUnitario, categoria_idCategoria) VALUES (%s, %s, %s)", (produto, valorUnitario, categoria,))
                self.conn.commit()
                time.sleep(1)
                print("Produto adicionado com sucesso!")
                time.sleep(0.7)
                print("\n[1] - Sim\n[2] - Não\n")
                escolha = int(input("Deseja adicionar mais ? "))

                if escolha == 1:
                    continue
                elif escolha == 2:
                    cursor.close()
                    break
                else:
                    print("Opção inválida! Tente novamente!")
                    continue
            except ValueError:
                print("Por favor, digite um valor válido!")


    # Função de atualização dos dados de um cliente
    def atualizar_cliente(self):
        try:
            while True:

                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM clientes;")
                self.rows = cursor.fetchall()

                if self.rows == []:
                    print("Opção inválida, pois não há clientes registrados!")
                    time.sleep(0.4)
                    print("Adicione um cliente primeiro!")
                    break
                else:
                    time.sleep(0.7)
                    print("\n[1] - Alterar somente nome do cliente\n[2] - Alterar somente idade do cliente\n[3] - Alterar todos os dados do cliente\n")
                    escolha = int(input("Escolha uma das opções acima: "))
        
                    if escolha == 1:
                        time.sleep(0.7)
                        cursor.execute("SELECT idCliente, nome FROM clientes;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        print("\n")
                        time.sleep(0.7)

                        idCliente = int(input("Escolha na lista de clientes qual nome você quer alterar pelo ID: "))
                        novoNome = input("Escolha um novo nome: ")

                        for id, nome in self.rows:
                            if idCliente == id:
                                cursor.execute("UPDATE clientes SET nome = %s WHERE idCliente = %s;", (novoNome, idCliente, ))
                                self.conn.commit()
                                nome = novoNome
                                print("Cliente teve seu nome alterado com sucesso!")
                                break

                        if nome != novoNome:
                            print("Cliente não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break

                    elif escolha == 2:
                        time.sleep(0.7)
                        cursor.execute("SELECT idCliente, nome, idade FROM clientes;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        print("\n")
                        time.sleep(0.7)

                        idCliente = int(input("Escolha na lista de clientes qual idade você quer alterar pelo ID: "))
                        novaIdade = int(input("Escolha uma nova idade: "))

                        for id, nome, idade in self.rows:
                            if id == idCliente:
                                cursor.execute("UPDATE clientes SET idade = %s WHERE idCliente = %s;", (novaIdade, idCliente, ))
                                self.conn.commit()
                                idade = novaIdade
                                print("Cliente teve sua idade alterada com sucesso!")
                                break

                        if idade != novaIdade:
                            print("Cliente não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break

                    elif escolha == 3:
                        time.sleep(0.7)
                        cursor.execute("SELECT idCliente, nome, idade FROM clientes;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        print("\n")
                        time.sleep(0.7)

                        idCliente = int(input("Escolha na lista de clientes qual nome e idade você quer alterar pelo ID: "))
                        novoNome = input("Escolha um novo nome: ")
                        novaIdade = int(input("Escolha uma nova idade: "))

                        for id, nome, idade in self.rows:
                            if id == idCliente:
                                cursor.execute("UPDATE clientes SET nome = %s, idade = %s WHERE idCliente = %s;", (novoNome, novaIdade, idCliente, ))
                                self.conn.commit()
                                nome = novoNome
                                idade = novaIdade
                                print("Cliente teve seu nome e idade alterados com sucesso!")
                                break
                            
                        if nome != novoNome and idade != novaIdade:
                            print("Cliente não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break
                    
                    else:
                        print("Por favor, digite uma opção válida!")
                        continue
        except ValueError:
            print("Por favor, digite um valor válido!")
            self.atualizar_cliente()

    # Função de atualização dos dados de um produto
    def atualizar_produtos(self):
        try:
            while True:

                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM produtos;")
                self.rows = cursor.fetchall()

                if self.rows == []:
                    print("Opção inválida, pois não há produtos registrados!")
                    time.sleep(0.4)
                    print("Adicione um produto primeiro!")
                    break
                else:
                    time.sleep(0.7)
                    print("\n[1] - Alterar somente descrição do produto\n[2] - Alterar somente o valor unitário do produto\n[3] - Alterar somente a categoria do produto\n[4] - Alterar todos os dados do produto")
                    escolha = int(input("Escolha uma das opções acima: "))
            
                    if escolha == 1:
                        time.sleep(0.7)
                        cursor.execute("SELECT idProduto, descricao FROM produtos;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        time.sleep(0.7)
                        print("\n")

                        idProduto = int(input("Digite o ID do produto que gostaria de alterar: "))
                        novaDescricao = input("Digite a nova descrição do produto: ").upper()

                        for id, produto in self.rows:
                            if idProduto == id:
                                cursor.execute("UPDATE produtos SET descricao = %s WHERE idProduto = %s;", (novaDescricao, idProduto,))
                                self.conn.commit()
                                id = idProduto
                                print("Produto alterado com sucesso!")
                                break
                            
                        if id != idProduto:
                            print("Produto não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break

                    elif escolha == 2:
                        time.sleep(0.7)
                        cursor.execute("SELECT idProduto, descricao, valorUnitario FROM produtos;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        time.sleep(0.7)
                        print("\n")

                        idProduto = int(input("Digite o ID do produto que gostaria de alterar: "))
                        novoValor = float(input("Digite o novo valor unitário do produto: "))

                        for id, produto, valor in self.rows:
                            if idProduto == id:
                                cursor.execute("UPDATE produtos SET valorUnitario = %s WHERE idProduto = %s;", (novoValor, idProduto,))
                                self.conn.commit()
                                id = idProduto
                                print("Valor unitário alterado com sucesso!")
                                break

                        if id != idProduto:
                            print("Produto não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break

                    elif escolha == 3:
                        time.sleep(0.7)
                        cursor.execute("SELECT pr.idProduto, pr.descricao AS produto, ca.idCategoria, ca.descricao AS categoria FROM produtos pr INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria ORDER BY pr.idProduto;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        time.sleep(0.7)
                        print("\n")

                        idProduto = int(input("Digite o ID do produto que gostaria de alterar: "))
                        novaCategoria = int(input("Digite a nova categoria do produto por ID: "))

                        for idproduto, produto, idcategoria, categoria in self.rows:
                            if idProduto == idproduto:
                                cursor.execute("UPDATE produtos SET categoria_idCategoria = %s WHERE idProduto = %s;", (novaCategoria, idProduto,))
                                self.conn.commit()
                                idproduto = idProduto
                                print("Categoria alterada com sucesso!")
                                break
                            
                        if idproduto != idProduto:
                            print("Produto não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break

                    elif escolha == 4:
                        time.sleep(0.7)
                        cursor.execute("SELECT pr.idProduto, pr.descricao AS produto, pr.valorUnitario, ca.idCategoria, ca.descricao AS categoria FROM produtos pr INNER JOIN categorias ca ON pr.categoria_idCategoria = ca.idCategoria ORDER BY pr.idProduto;")
                        self.columms = [desc[0] for desc in cursor.description]
                        self.rows = cursor.fetchall()
                        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                        time.sleep(0.7)
                        print("\n")

                        idProduto = int(input("Digite o ID do produto que gostaria de alterar: "))
                        novaDescricao = input("Digite a nova descrição do produto: ").upper()
                        novoValor = float(input("Digite o novo valor unitário do produto: "))
                        novaCategoria = int(input("Digite a nova categoria do produto por ID: "))

                        for idproduto, produto, valor, idcategoria, categoria in self.rows:
                            if idProduto == idproduto:
                                cursor.execute("UPDATE produtos SET descricao = %s, valorUnitario = %s, categoria_idCategoria = %s WHERE idProduto = %s;", (novaDescricao, novoValor, novaCategoria, idProduto,))
                                self.conn.commit()
                                idproduto = idProduto
                                produto = novaDescricao
                                valor = novoValor
                                idcategoria = novaCategoria
                                print("Todos os dados do produto foram alterados com sucesso!")

                        if idproduto != idProduto and produto != novaDescricao and valor != novoValor and idcategoria != novaCategoria:
                            print("Produto não encontrado! Tente novamente!")
                            continue
                        else:
                            cursor.close()
                            break
                    else:
                        print("Por favor, selecione uma opção válida!")
                        continue
        except ValueError:
            print("Por favor, digite um valor válido!")

    # Função de deletar um cliente
    def deletar_cliente(self):
        while True:

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM clientes;")
            self.rows = cursor.fetchall()

            if self.rows == []:
                print("Opção inválida, pois não há clientes registrados!")
                time.sleep(0.4)
                print("Adicione um cliente primeiro!")
                break
            else:
                time.sleep(0.7)
                print("\n")
                cursor = self.conn.cursor()
                cursor.execute("SELECT idCliente, nome FROM clientes;")
                self.columms = [desc[0] for desc in cursor.description]
                self.rows = cursor.fetchall()
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                time.sleep(0.7)
                print("\n")
                try:
                    clienteDeletado = int(input("Escolha na lista de clientes quem você quer deletar pelo ID: "))

                    for id, nome in self.rows:
                        if clienteDeletado == id:
                            cursor.execute("DELETE FROM clientes WHERE idCliente = %s;", (clienteDeletado,))
                            self.conn.commit()
                            id = clienteDeletado
                            print(f"Cliente {nome} deletado com sucesso!")
                            cursor.execute("ALTER TABLE clientes AUTO_INCREMENT = %s;", (clienteDeletado,))
                            break

                    if id != clienteDeletado:
                        print("Cliente não encontrado! Tente novamente!")
                        continue
                    else:
                        cursor.close()
                        break
                except ValueError:
                    print("Por favor, digite um número válido!")
                    continue
    
    # Função de deletar um produto
    def deletar_produto(self):
        while True:

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM produtos;")
            self.rows = cursor.fetchall()

            if self.rows == []:
                print("Opção inválida, pois não há produtos registrados!")
                time.sleep(0.4)
                print("Adicione um produto primeiro!")
                break
            else:
                time.sleep(0.7)
                print("\n")
                cursor = self.conn.cursor()
                cursor.execute("SELECT p.idProduto, p.descricao AS produto, p.valorUnitario, c.descricao AS categoria " \
                "FROM produtos p JOIN categorias c ON p.categoria_idCategoria = c.idCategoria;")
                self.columms = [desc[0] for desc in cursor.description]
                self.rows = cursor.fetchall()
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                time.sleep(0.7)
                print("\n")
                try:
                    produtoDeletado = int(input("Escolha na lista de produtos qual você quer deletar pelo ID: "))

                    for id, produto, valoUnitario, categoria in self.rows:
                        if produtoDeletado == id:
                            cursor.execute("DELETE FROM produtos WHERE idProduto = %s;", (produtoDeletado,))
                            self.conn.commit()
                            id = produtoDeletado
                            print("Produto deletado com sucesso!")
                            cursor.execute("ALTER TABLE produtos AUTO_INCREMENT = %s;", (produtoDeletado,))
                            self.conn.commit()
                            break
                    
                    if id != produtoDeletado:
                        print("Produto não encontrado! Tente novamente!")
                        continue
                    else:
                        cursor.close()
                        break
                except ValueError:
                    print("Por favor, digite um número válido!")

    def deletar_pedido(self):
        while True:
            time.sleep(1)
            cursor = self.conn.cursor()
            cursor.execute("SELECT p.idPedido, cl.nome AS cliente, it.quantidade, pr.descricao AS produto, pr.valorUnitario, it.valorTotal, pa.descricao AS formaPagamento FROM pedidos p INNER JOIN clientes cl ON p.cliente_idCliente = cl.idCliente " \
            "INNER JOIN itenspedidos it ON it.pedido_idPedido = p.idPedido " \
            "INNER JOIN produtos pr ON it.produto_idProduto = pr.idProduto " \
            "INNER JOIN pagamento pa ON p.pagamento_idPagamento = pa.idPagamento ORDER BY p.idPedido;")
            self.columms = [desc[0] for desc in cursor.description]
            self.rows = cursor.fetchall()

            if self.rows == []:
                print("Não há pedidos registrados!")
                break
            else:
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                print("\n")
                pedidoDeletado = int(input("Escolha pelo ID qual pedido você quer deletar: "))
                for id, cliente, quantidade, produto, valorUn, valorTot, pagamento in self.rows:
                    if pedidoDeletado == id:
                        cursor.execute("DELETE FROM pedidos WHERE idPedido = %s;", (pedidoDeletado,))
                        self.conn.commit()
                        id = pedidoDeletado
                        print("Pedido deletado com sucesso!")
                        cursor.execute("ALTER TABLE pedidos AUTO_INCREMENT = %s;", (pedidoDeletado,))
                        break

                if id != pedidoDeletado:
                    print("ID inválido! Tente novamente!")
                    continue
                else:
                    cursor.close()
                    break

    # Função de limpeza total da tabela clientes
    def limpar_clientes(self):
        time.sleep(0.7)
        cursor = self.conn.cursor()
        print("Desativando restrições de chaves estrangeiras temporariamente...")
        time.sleep(1)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        print("Limpando a tabela clientes...")
        time.sleep(1)
        cursor.execute("TRUNCATE TABLE clientes;")
        print("Tabela clientes limpa com sucesso!")
        time.sleep(0.5)
        print("Reativando restrições de chaves estrangeiras...")
        time.sleep(0.6)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.conn.commit()
        cursor.close()

    # Função de limpeza total da tabela produtos
    def limpar_produtos(self):
        time.sleep(0.7)
        cursor = self.conn.cursor()
        print("Desativando restrições de chaves estrangeiras temporariamente...")
        time.sleep(1)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        print("Limpando a tabela produtos...")
        time.sleep(1)
        cursor.execute("TRUNCATE TABLE produtos;")
        print("Tabela produtos limpa com sucesso!")
        time.sleep(0.5)
        print("Reativando restrições de chaves estrangeiras...")
        time.sleep(0.6)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        self.conn.commit()
        cursor.close()

    # Função de limpeza total da tabela pedidos
    def limpar_pedidos(self):
        time.sleep(0.7)
        cursor = self.conn.cursor()
        print("Desativando restrições de chaves estrangeiras temporariamente...")
        time.sleep(1)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        print("Limpando a tabelas pedidos...")
        time.sleep(1)
        cursor.execute("TRUNCATE TABLE pedidos;")
        print("Tabela pedidos limpa com sucesso!")
        time.sleep(0.5)
        print("Reativando restrições de chaves estrangeiras...")
        time.sleep(0.6)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.conn.commit()
        cursor.close()
      