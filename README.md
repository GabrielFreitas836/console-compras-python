# 📦 Sobre o projeto

### Neste repositório, você encontrará os arquivos para o desenvolvimento de uma aplicação de console criada em Python.

A aplicação simula o gerenciamento de compras e estoque de um supermercado.

## 🧑‍🛒 Cliente
- Ao simular um cliente, será possível:

  - Escolher produtos;

  - Adicioná-los ao carrinho de compras;

  - Selecionar o método de pagamento.

## 🧑‍💼 Gerente
- Ao simular o gerente, será possível:

  - Gerenciar o estoque;

  - Adicionar novos produtos;

  - Consultar o saldo diário (com base nas compras realizadas pelos clientes).

---
## 🗄️ Conexão com MySQL
### Sobre o banco de dados
Todos os dados utilizados na simulação do console terão origem em um banco criado no MySQL. Escolhi esse banco relacional por ser uma solução estável e eficiente para organizar dados estruturados, como clientes, produtos e vendas. O MySQL garante a integridade dos dados por meio de relacionamentos entre tabelas, facilitando consultas e atualizações consistentes. Além disso, é amplamente suportado, possui boa performance e permite o crescimento seguro do projeto.

### Como criar a conexão
Para criar a conexão, será necessário:

- Instalar o driver com:

  `pip install mysql-connector-python`
- Importar o módulo no seu código:

  `import mysql.connector`
- Utilizar uma função para configurar as credenciais de acesso ao banco:

  - User
  - Host
  - Database
  - Password

### OBS:
## Para maior segurança, os dados da conexão serão armazenados em um arquivo .env.
---
