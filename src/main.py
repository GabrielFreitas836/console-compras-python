"""
    arquivo: main.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descrição: arquivo principal para execução do programa
"""

# Importando a classe Menu de interacao_principal.py
from menu.interacao_principal import Menu
# Importando a biblioteca de conexão com o MySQL
import mysql.connector
# Importando dotenv para manter os dados de conexão do banco seguros
from dotenv import load_dotenv
# Importando módulo necessário para acessar as variáveis de ambiente carregadas pelo dotenv
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

    # Execução da função principal do programa que roda todas asoutras funções necessárias para seu funcionamento completo
    # Uso de try/except para interromper a execução caso aconteca algum erro
    try:
        m.menu(bd_config)
    except mysql.connector.Error as error:
        print("Erro de Banco de Dados: ", error)
    except mysql.connector.InterfaceError as error:
        print("Erro de Interface do MySQL: ", error)
    except Exception as error:
        print("Outro tipo de erro: ", error)
        