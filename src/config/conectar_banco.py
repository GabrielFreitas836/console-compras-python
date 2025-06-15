"""
    arquivo: conectar_banco.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descrição: conexão com o banco MySQL
"""

# Importando o driver de conexão com o MySQL
import mysql.connector

# Classe responsável por fazer a conexão com o banco MySQL
class ConectarBanco:
    
    # Função inicializadora que define a conexão do banco nula
    def __init__(self):
        self.conn = None

    # Função de conexão com o banco de dados
    # Verificação de conexão fechada ou inexistente para abrir essa conexão
    def conectar_ao_banco(self, bd_config):
        if self.conn is None or not self.conn.is_connected():
            self.bd_config = bd_config
            self.conn = mysql.connector.connect(**self.bd_config)
            print("Banco conectado com sucesso")
        else:
            pass
        return self.conn
    
    # Função que fecha a conexão com o banco de dados
    def fechar_conexao(self):
        print("Banco fechado com sucesso")
        self.conn.close()
        