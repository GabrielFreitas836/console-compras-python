"""
    arquivo: main.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descrição: arquivo principal para execução do programa
"""

# Importando a classe de conectar_banco.py
from menu.interacao_principal import Menu
import mysql.connector
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    m = Menu()
    load_dotenv()
    bd_config = {
        'host': os.getenv("DB_HOST"),
        'user': os.getenv("DB_USER"),
        'port': 3306,
        'password': os.getenv("DB_PASSWORD"),
        'database': os.getenv("DB_DATABASE")
    }

    try:
        m.menu(bd_config)
    except mysql.connector.Error as error:
        print("Erro de Banco de Dados: ", error)
    except mysql.connector.InterfaceError as error:
        print("Erro de Interface do MySQL: ", error)
    except Exception as error:
        print("Outro tipo de erro: ", error)
        