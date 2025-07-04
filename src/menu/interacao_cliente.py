"""
    arquivo: interacao_cliente.py
    autor: Gabriel Freitas
    data: 15/06/2025
    descricao: interações relacionadas ao cliente na aplicação console

"""

from config.conectar_banco import ConectarBanco
from menu.controle_compras import Compras
from tabulate import tabulate
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Cliente(ConectarBanco):
    def __init__(self, conn = None):
        super().__init__()
        self.conn = conn
        self.compras = Compras(self.conn)

    # Função de carregar os dados da tabela 'clientes'
    def carregar_clientes(self, bd_config):
        self.bd_config = bd_config
        cursor = self.conn.cursor()
        cursor.execute("SELECT idCliente, nome FROM clientes")
        self.columms = [desc[0] for desc in cursor.description]
        self.rows = cursor.fetchall()

    # Função de registro de clientes para as duas situações possíveis: quando não há cliente registrado e quando há cliente(s) registrado(os)
    # Se houver clientes registrados, ele mostrará em interacao_principal a tabela de clientes com os dados existentes
    def registrar_cliente(self):
        if self.rows == []:
            registrar_sistema = int(input("Não há algum cliente registrado! Gostaria de se registrar no sistema ? "))
            if registrar_sistema == 2:
                print("=" *50)
                print("Sem problemas! Retornando ao início...")
                time.sleep(0.7)
                return True
            elif registrar_sistema == 1:
                print("=" *50)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(0.7)
                print(f"Cliente {nome} adicionado(a) com sucesso!")
                self.escolher_cliente()
                return True
            else:
                print("=" *50)
                print("Por favor, digite [1] para se registrar ou [2] para retornar ao início")
                return True
        else:
            registrar_sistema = int(input("Gostaria de se registrar como outro cliente ? "))
            if registrar_sistema == 2:
                print("=" *50)
                time.sleep(1)
                return True
            elif registrar_sistema == 1:
                print("=" *50)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(0.7)
                print(f"Cliente {nome} adicionado(a) com sucesso!")
                return True
            else:
                time.sleep(0.7)
                print("=" *50)
                print("Por favor, digite [1] para se registrar ou [2] para escolher seu usuário")
                print("\n")
                self.carregar_clientes(self.bd_config)
                print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                self.registrar_cliente()
                return True
    
    # Função de escolher qual cliente está utilizando o sistema
    # Utilizando o loop for para iterar por todos os IDs do banco até achar por aquele que é igual à escolha do usuário
    def escolher_cliente(self):
        while True:
            time.sleep(0.7)
            print("\n")
            self.carregar_clientes(self.bd_config)
            print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))

            try:
                print("\n")
                escolha = int(input("Escolha na lista de clientes quem é você pelo ID: "))
            except ValueError:
                print("Por favor, digite um número válido!")
                continue

            for id, nome in self.rows:
                if escolha == id:
                    self.compras.carregar_produtos()
                    self.compras.adicionar_ao_carrinho(escolha)
                    id = escolha
                    break
                
            if id != escolha:
                print("Cliente não encontrado! Tente novamente!")
                continue
            else:
                return True
