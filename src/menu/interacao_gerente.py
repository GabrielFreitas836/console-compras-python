"""
    arquivo: interacao_gerente.py
    autor: Gabriel Freitas
    data: 16/06/2025
    descricao: interações relacionadas ao gerente na aplicação console
"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Gerente(ConectarBanco):
    def __init__(self, conn = None):
        super().__init__()
        self.conn = conn

    # Função principal que gerencia as opções do gerente
    def opcoes_gerente(self):
        print("\n[1] - Clientes\n[2] - Produtos\n")
        escolha = int(input("Em qual categoria gostaria de mexer ? "))

        match escolha:
            case 1:
                print("Abrindo aba de clientes...")
                time.sleep(1)
                print("=" *50)
                print("\n[1] - Adicionar um novo cliente\n[2] - Alterar dados de um cliente existente\n[3] - Deletar um cliente existente\n")
                subescolha = int(input("O que você gostaria de fazer ? "))
                print("=" *50)

                if subescolha == 1:
                    nome = input("Digite o nome do cliente: ")
                    idade = int(input("Digite a idade do cliente: "))
                    cursor = self.conn.cursor()
                    cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                    self.conn.commit()
                    time.sleep(1)
                    print(f"Cliente {nome} adicionado com sucesso!")
                elif subescolha == 2:
                    self.atualizar_cliente()
                elif subescolha == 3:
                    time.sleep(1)
                    print("\n")
                    cursor = self.conn.cursor()
                    cursor.execute("SELECT idCliente, nome FROM clientes")
                    self.columms = [desc[0] for desc in cursor.description]
                    self.rows = cursor.fetchall()
                    print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                    time.sleep(1)
                    while True:
                        print("\n")
                        try:
                            clienteDeletado = int(input("Escolha na lista de clientes quem você quer deletar pelo ID: "))
                        except ValueError:
                            print("Por favor, digite um número válido!")
                            continue

                        for id, nome in self.rows:
                            if clienteDeletado == id:
                                cursor.execute("DELETE FROM clientes WHERE idCliente = %s", (clienteDeletado,))
                                self.conn.commit()
                                print(f"Cliente {nome} deletado com sucesso")
                                break
                        
                        print("Cliente não encontrado! Tente novamente!")
                    
            case 2:
                print("Abrindo aba de produtos...")
                time.sleep(1)
                print("=" *50)
                print("\n[1] - Adicionar um novo produto\n[2] - Alterar dados de um produto existente\n[3] - Deletar um produto existente\n")
                print("=" *50)
            case _:
                print("Escolha 1 ou 2")

    # Função de atualização dos dados de um cliente
    def atualizar_cliente(self):
        time.sleep(1)
        print("\n[1] - Alterar somente nome do cliente\n[2] - Alterar somente idade do cliente\n[3] - Alterar todos os dados do cliente\n")
        escolha = int(input("Escolha uma das opções acima: "))
        if escolha == 1:
            time.sleep(1)
            print("=" *50)
            cursor = self.conn.cursor()
            cursor.execute("SELECT idCliente, nome FROM clientes")
            self.columms = [desc[0] for desc in cursor.description]
            self.rows = cursor.fetchall()
            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
            print("\n")
            time.sleep(1)
            while True:
                try:
                    idCliente = int(input("Escolha na lista de clientes qual nome você quer alterar pelo ID: "))
                    novoNome = input("Escolha um novo nome: ")
                except ValueError:
                    print("Por favor, digite um número válido!")
                    continue

                for id, nome in self.rows:
                    if idCliente == id:
                        cursor = self.conn.cursor()
                        cursor.execute("UPDATE clientes SET nome = %s WHERE idCliente = %s", (novoNome, idCliente, ))
                        self.conn.commit()
                        nome = novoNome
                        print("Cliente teve seu nome alterado com sucesso!")
                        break

                if nome != novoNome:
                    print("Cliente não encontrado! Tente novamente!")
                    continue
                else:
                    break

        elif escolha == 2:
            time.sleep(1)
            cursor = self.conn.cursor()
            cursor.execute("SELECT idCliente, nome, idade FROM clientes")
            self.columms = [desc[0] for desc in cursor.description]
            self.rows = cursor.fetchall()
            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
            print("\n")
            time.sleep(1)
            while True:
                try:
                    idCliente = int(input("Escolha na lista de clientes qual idade você quer alterar pelo ID: "))
                    novaIdade = int(input("Escolha uma nova idade: "))
                except ValueError:
                    print("Por favor, digite um número válido!")
                    continue

                for id, nome, idade in self.rows:
                    if id == idCliente:
                        cursor = self.conn.cursor()
                        cursor.execute("UPDATE clientes SET idade = %s WHERE idCliente = %s", (novaIdade, idCliente, ))
                        self.conn.commit()
                        idade = novaIdade
                        print("Cliente teve sua idade alterada com sucesso!")
                        break

                if idade != novaIdade:
                    print("Cliente não encontrado! Tente novamente!")
                    continue
                else:
                    break

        elif escolha == 3:
            time.sleep(1)
            cursor = self.conn.cursor()
            cursor.execute("SELECT idCliente, nome, idade FROM clientes")
            self.columms = [desc[0] for desc in cursor.description]
            self.rows = cursor.fetchall()
            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
            print("\n")
            time.sleep(1)
            while True:
                try:
                    idCliente = int(input("Escolha na lista de clientes qual nome e idade você quer alterar pelo ID: "))
                    novoNome = input("Escolha um novo nome: ")
                    novaIdade = int(input("Escolha uma nova idade: "))
                except ValueError:
                    print("Por favor, digite um número válido!")
                    continue

                for id, nome, idade in self.rows:
                    if id == idCliente:
                        cursor = self.conn.cursor()
                        cursor.execute("UPDATE clientes SET nome = %s, idade = %s WHERE idCliente = %s", (novoNome, novaIdade, idCliente, ))
                        self.conn.commit()
                        nome = novoNome
                        idade = novaIdade
                        print("Cliente teve seu nome e idade alterados com sucesso!")
                        break
                
                if nome != novoNome and idade != novaIdade:
                    print("Cliente não encontrado! Tente novamente!")
                    continue
                else:
                    break
