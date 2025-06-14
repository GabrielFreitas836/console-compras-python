"""
    arquivo: main.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descrição: arquivo principal para execução do programa
"""

# Importando a classe de conectar_banco.py
from config.conectar_banco import ConectarBanco

import mysql.connector

if __name__ == "__main__":
    c = ConectarBanco()
    bd_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'GgFf19072005#@',
        'database': 'sistema_mercado'
    }

    try:
        c.conectar_ao_banco(bd_config)
        c.fechar_conexao()
    except mysql.connector.Error as error:
        print("Erro de Banco de Dados: ", error)
    except mysql.connector.InterfaceError as error:
        print("Erro de interface do MySQL: ", error)
    except Exception as error:
        print("Outro tipo de erro: ", error)
