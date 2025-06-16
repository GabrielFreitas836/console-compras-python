"""
    arquivo: interacao_gerente.py
    autor: Gabriel Freitas
    data: 16/06/2025
    descricao: interações relacionadas ao gerente na aplicação console
"""

from config.conectar_banco import ConectarBanco
from tabulate import tabulate
import time

# Função inicializadora da classe + init da classe ConectarBanco
class Gerente(ConectarBanco):
    def __init__(self):
        super().__init__()

    