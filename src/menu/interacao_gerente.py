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
                    print("Update em breve...")
                elif subescolha == 3:
                    time.sleep(1)
                    print("\n")
                    cursor = self.conn.cursor()
                    cursor.execute("SELECT idCliente, nome FROM clientes")
                    self.columms = [desc[0] for desc in cursor.description]
                    self.rows = cursor.fetchall()
                    print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                    time.sleep(1)
                    print("\n")
                    clienteDeletado = int(input("Escolha na lista de clientes quem você quer deletar pelo ID: "))
                    for id, nome in self.rows:
                        if clienteDeletado == id:
                            cursor.execute("DELETE FROM clientes WHERE idCliente = %s", (clienteDeletado,))
                            self.conn.commit()
                            print(f"Cliente {nome} deletado com sucesso")
                    
            case 2:
                print("Abrindo aba de produtos...")
                time.sleep(1)
                print("=" *50)
                print("\n[1] - Adicionar um novo produto\n[2] - Alterar dados de um produto existente\n[3] - Deletar um produto existente\n")
                print("=" *50)
            case _:
                print("Escolha 1 ou 2")
