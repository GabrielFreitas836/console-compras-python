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

    def opcoes_gerente(self):
        print("\n[1] - Clientes\n[2] - Produtos\n")
        escolha = int(input("Em qual categoria gostaria de mexer ? "))

        match escolha:
            case 1:
                print("Abrindo aba de clientes...")
                time.sleep(1)
                print("=" *50)
                print("\n[1] - Adicionar um novo cliente\n[2] - Alterar dados de um cliente existente\n[3] - Deletar um cliente existente\n")
                print("=" *50)
            case 2:
                print("Abrindo aba de produtos...")
                time.sleep(1)
                print("=" *50)
                print("\n[1] - Adicionar um novo produto\n[2] - Alterar dados de um produto existente\n[3] - Deletar um produto existente\n")
                print("=" *50)
            case _:
                print("Escolha 1 ou 2")
