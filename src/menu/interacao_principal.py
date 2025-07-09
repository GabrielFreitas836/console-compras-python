"""
    arquivo: interacao_principal.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descricao: interações principais da aplicação console

"""

# Importando a classe ConectarBanco de conectar_banco.py
from config.conectar_banco import ConectarBanco
# Importando as classes Cliente e Gerente de interacao_cliente.py e interacao_gerente.py
from menu.interacao_cliente import Cliente
from menu.interacao_gerente import Gerente
# Biblioteca usada para formatar os resultados das consultas SQL
from tabulate import tabulate
# Biblioteca usada para criar pausas na execução , útil para simular procesamento ou melhorar a visualização
# Utilização com time.sleep
import time

class Menu:

    # Função inicializadora da classe
    # Instancia as class Cliente e Gerente
    def __init__(self):
        self.cliente = Cliente()
        self.gerente = Gerente()

    # Função principal da aplicação que coordena toda a lógica do programa, utilizando as funções advindas de interacao_cliente e interacao_gerente
    def menu(self, bd_config):
        while True:
            banco = ConectarBanco()
            banco.conectar_ao_banco(bd_config)
            self.bd_config = bd_config
            self.cliente = Cliente(conn = banco.conn)
            self.gerente = Gerente(conn = banco.conn)
            print("=" *60)
            print("Olá! Seja bem-vindo(a) ao sistema de gerenciamento!")
            print("\n[1] - Cliente\n[2] - Gerente\n[3] - Fechar o programa\n")
            entidade = int(input("Você é cliente ou gerente ? Aperte 1,2 ou 3 se for fechar o programa "))
            if entidade == 1:
                time.sleep(0.2)
                print("Carregando lista de clientes...")
                self.cliente.carregar_clientes(bd_config)
                time.sleep(0.7)
                if self.cliente.rows == []:
                    print("=" *50)
                    print("\n[1] - sim\n[2] - não\n")
                    continuarRegistro = self.cliente.registrar_cliente()

                    if not continuarRegistro:
                        self.cliente.fechar_conexao()
                        break
                    
                else:
                    print(tabulate(self.cliente.rows, headers=self.cliente.columms, tablefmt="grid"))
                    time.sleep(0.7)    
                    print("\n[1] - sim\n[2] - não\n")
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
                inicio = self.gerente.opcoes_gerente()
                if inicio:
                    continue
                else:
                    self.gerente.fechar_conexao()
                    break
            elif entidade == 3:
                print("Fechando o programa...")
                time.sleep(0.5)
                banco.fechar_conexao()
                break
            else:
                print("Por favor, digite [1] se for cliente ou [2] se for gerente")
                time.sleep(0.8)
                print("Retornando ao início...")
                time.sleep(1)
                continue        
