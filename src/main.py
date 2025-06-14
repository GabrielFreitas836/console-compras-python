"""
    arquivo: main.py
    autor: Gabriel Freitas
    data: 14/06/2025
    descrição: arquivo principal para execução do programa
"""

# Importando a classe de conectar_banco.py
from config.conectar_banco import ConectarBanco

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
    except Exception as error:
        print("Erro ao fazer a conexão: ", error)