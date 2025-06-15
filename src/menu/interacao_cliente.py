"""
    arquivo: interacao_cliente.py
    autor: Gabriel Freitas
    data: 15/06/2025
    descricao: interações relacionadas ao cliente na aplicação console

"""

from config.conectar_banco import ConectarBanco
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Cliente(ConectarBanco):
    def __init__(self):
        super().__init__()

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
                print("=" *30)
                print("Sem problemas! Até mais!")
                ConectarBanco.fechar_conexao(self)
                return False
            elif registrar_sistema == 1:
                print("=" *30)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(1)
                print(f"Cliente {nome} adicionado com sucesso!")
                return True
            else:
                print("=" *30)
                print("Por favor, digite [1] para se registrar ou [2] para sair do sistema")
                return True
        else:
            registrar_sistema = int(input("Gostaria de se registrar como outro cliente ? "))
            if registrar_sistema == 2:
                print("=" *30)
                print("Sem problemas! Até mais!")
                ConectarBanco.fechar_conexao(self)
                return False
            elif registrar_sistema == 1:
                print("=" *30)
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                self.conn.commit()
                time.sleep(1)
                print(f"Cliente {nome} adicionado com sucesso!")
                return True
            else:
                print("=" *30)
                print("Por favor, digite [1] para se registrar ou [2] para sair do sistema")
                return True

        