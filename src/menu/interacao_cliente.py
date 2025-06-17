"""
    arquivo: interacao_cliente.py
    autor: Gabriel Freitas
    data: 15/06/2025
    descricao: interações relacionadas ao cliente na aplicação console

"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Cliente(ConectarBanco):
    def __init__(self, conn = None):
        super().__init__()
        self.conn = conn

    def carregar_clientes(self, bd_config):
        self.bd_config = bd_config
        cursor = self.conn.cursor()
        cursor.execute("SELECT idCliente, nome FROM clientes")
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()

    def registrar_cliente(self):
        if self.rows == []:
            registrar_sistema = int(input("Não há algum cliente registrado! Gostaria de se registrar no sistema ? "))
            if registrar_sistema == 2:
                print("=" *50)
                print("Sem problemas! Retornando ao início...")
                time.sleep(1.5)
                return True
            elif registrar_sistema == 1:
                print("=" *50)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(1)
                print(f"Cliente {nome} adicionado com sucesso!")
                return True
            else:
                print("=" *50)
                print("Por favor, digite [1] para se registrar ou [2] para sair do sistema")
                return True
        else:
            registrar_sistema = int(input("Gostaria de se registrar como outro cliente ? "))
            if registrar_sistema == 2:
                print("=" *50)
                time.sleep(1.5)
                return True
            elif registrar_sistema == 1:
                print("=" *50)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(1)
                print(f"Cliente {nome} adicionado com sucesso!")
                return True
            else:
                print("=" *50)
                print("Por favor, digite [1] para se registrar ou [2] para sair do sistema")
                return True
    
    def escolher_cliente(self):
        time.sleep(1.5)
        Cliente.carregar_clientes(self, self.bd_config)
        print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
        escolha = int(input("Escolha na lista de clientes quem é você pelo ID: "))
        for id, nome in self.rows:
            if escolha == id:
                print(f"Olá, {nome}!")
                return False