"""
    arquivo: interacao_principal.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descricao: interações principais da aplicação console

"""

from menu.interacao_cliente import Cliente
from menu.interacao_gerente import Gerente
from tabulate import tabulate
import time

class Menu:

    def __init__(self):
        self.cliente = Cliente()
        self.gerente = Gerente()

    def menu(self, bd_config):
        while True:
            self.bd_config = bd_config
            self.cliente.conectar_ao_banco(bd_config)
            self.gerente.conectar_ao_banco(bd_config)
            print("=" *50)
            print("Olá! Seja bem-vindo(a) ao sistema de gerenciamento!")
            print("\n [1] - cliente\n [2] - gerente\n")
            entidade = int(input("Você é cliente ou gerente ? Aperte 1 ou 2 "))
            if entidade == 1:
                time.sleep(0.2)
                print("Carregando lista de clientes...")
                self.cliente.carregar_clientes(bd_config)
                time.sleep(1)
                if self.cliente.rows == []:
                    print("=" *50)
                    print("\n [1] - sim\n [2] - não\n")
                    continuarRegistro = self.cliente.registrar_cliente()
                    if not continuarRegistro:
                        self.cliente.fechar_conexao()
                        break

                    continuarEscolha = self.cliente.escolher_cliente()
                    if not continuarEscolha:
                        self.cliente.fechar_conexao()
                        break
                else:
                    print(tabulate(self.cliente.rows, headers=self.cliente.columms, tablefmt="grid"))
                    time.sleep(1)    
                    print("\n [1] - sim\n [2] - não\n")
                    continuarRegistro = self.cliente.registrar_cliente()
                    if not continuarRegistro:
                        self.cliente.fechar_conexao()
                        break

                    continuarEscolha = self.cliente.escolher_cliente()
                    if not continuarEscolha:
                        self.cliente.fechar_conexao()
                        break
            elif entidade == 2:
                time.sleep(0.2)
                print("=" *50)
                print("Bem-vindo, gerente!")
                self.gerente.opcoes_gerente()
                self.gerente.fechar_conexao()
                break
            else:
                print("Por favor, digite [1] se for cliente ou [2] se for gerente")
                time.sleep(0.8)
                print("Retornando ao início...")
                time.sleep(1.5)
                continue        
