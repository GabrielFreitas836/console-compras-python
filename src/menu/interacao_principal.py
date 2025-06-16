"""
    arquivo: interacao_principal.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descricao: interações principais da aplicação console

"""

from menu.interacao_cliente import Cliente
from tabulate import tabulate
import time

class Menu(Cliente):

    # Função inicializadora da classe + init da classe Cliente
    def __init__(self):
        super().__init__()

    def menu(self, bd_config):
        while True:
            self.bd_config = bd_config
            self.conectar_ao_banco(bd_config)
            print("=" *30)
            print("Olá! Seja bem-vindo(a) ao sistema de gerenciamento!")
            print("\n [1] - cliente\n [2] - gerente\n")
            entidade = int(input("Você é cliente ou gerente ? Aperte 1 ou 2 "))
            if entidade == 1:
                print("Carregando lista de clientes...")
                Cliente.carregar_clientes(self, bd_config)
                time.sleep(1)
                if self.rows == []:
                    print("=" *30)
                    print("\n [1] - sim\n [2] - não\n")
                    continuarRegistro = Cliente.registrar_cliente(self)
                    if not continuarRegistro:
                        break

                    continuarEscolha = Cliente.escolher_cliente(self)
                    if not continuarEscolha:
                        break
                else:
                    print(tabulate(self.rows, headers=self.columms, tablefmt="grid"))
                    time.sleep(1)    
                    print("\n [1] - sim\n [2] - não\n")
                    continuarRegistro = Cliente.registrar_cliente(self)
                    if not continuarRegistro:
                        break
                    
                    continuarEscolha = Cliente.escolher_cliente(self)
                    if not continuarEscolha:
                        break
            elif entidade == 2:
                print("Bem-vindo, gerente!")
                break
            else:
                print("Por favor, digite [1] se for cliente ou [2] se for gerente")
                time.sleep(0.8)
                print("Retornando ao início...")
                time.sleep(1.5)
                continue        
