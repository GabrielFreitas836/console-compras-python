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
    

    # Função de conexão com o banco de dados
    def conectar_ao_banco(self, bd_config):
        self.bd_config = bd_config
        self.conn = mysql.connector.connect(**self.bd_config)
        print("Banco conectado com sucesso")
        return self.conn
    
    # Função que fecha a conexão com o banco de dados
    def fechar_conexao(self):
        self.conn.close()
        print("Banco fechado com sucesso")
        