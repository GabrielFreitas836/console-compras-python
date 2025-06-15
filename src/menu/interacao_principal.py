"""
    arquivo: interacao_principal.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descricao: interações principais da aplicação console

"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
import time

class Menu(ConectarBanco):
    def menu(self, bd_config):
        while True:
            self.bd_config = bd_config
            ConectarBanco.conectar_ao_banco(self, bd_config)
            print("=" *30)
            print("Olá! Seja bem-vindo(a) ao sistema de gerenciamento!")
            print("\n [1] - cliente\n [2] - gerente\n")
            entidade = int(input("Você é cliente ou gerente ? Aperte 1 ou 2 "))
            if entidade == 1:
                print("Carregando lista de clientes...")
                cursor = self.conn.cursor()
                cursor.execute("SELECT idCliente, nome FROM clientes")
                columms = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                time.sleep(1)
                if rows == []:
                    print("=" *30)
                    print("\n [1] - sim\n [2] - não\n")
                    registrar_sistema = int(input("Não há algum cliente registrado! Gostaria de se registrar no sistema ? "))
                    if registrar_sistema == 2:
                        print("=" *30)
                        print("Sem problemas! Até mais!")
                        ConectarBanco.fechar_conexao(self)
                        break
                    elif registrar_sistema == 1:
                        print("=" *30)
                        nome = input("Digite seu nome: ")
                        idade = int(input("Digite sua idade: "))
                        cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade,))
                        self.conn.commit()
                        time.sleep(1)
                        print(f"Cliente {nome} adicionado com sucesso!")
                    else:
                        print("=" *30)
                        print("Por favor, digite [1] para se registrar ou [2] para sair do sistema")
                else:
                    print(columms)
                    for row in rows:
                        print(tabulate(row, headers=columms, tablefmt="grid"))
