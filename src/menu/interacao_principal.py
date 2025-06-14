"""
    arquivo: interacao_principal.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descricao: interações principais da aplicação console

"""

from config.conectar_banco import ConectarBanco

class Menu(ConectarBanco):
    def menu(self):
        print("=" *30)
        print("Olá! Seja bem-vindo(a) ao sistema de gerenciamento!")
        print("\n [1] - cliente\n [2] - gerente\n")
        entidade = int(input("Você é cliente ou gerente ? Aperte 1 ou 2 "))
        if entidade == 1:
            print("Carregando lista de clientes...")
            cursor = self.conn.cursor()
            cursor.execute("SELECT idCliente, nome FROM clientes")
            rows = cursor.fetchall()
            print(rows)
