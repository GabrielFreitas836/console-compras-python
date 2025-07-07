# 📦 Sobre o projeto

### Console de gerenciamento de compras feito em Visual Studio Code.

A aplicação simula o gerenciamento de compras e estoque de um supermercado. Ao iniciar o programa, você terá a opção de prosseguir como cliente ou gerente.

Seguindo o caminho como cliente, você poderá simular a escolha de um ou mais produtos, encerrar as compras e realizar o pagamento com algumas outras opções no meio do caminho.

Seguindo o caminho de gerente, você terá o controle total sobre os dados registrados especificamente dos clientes, produtos e pedidos. Você, como gerente, terá acesso às abas de cliente e produtos
em que poderá adicionar, modificar e deletar os seus dados e à aba de itens e pedidos em que poderá apenas deletar os itens registrados nos pedidos dos clientes. As três abas oferecem a opção também de poder serem 
limpas totalmente pelo usuário como gerente

## 🧑‍🛒 Cliente
- Ao simular um cliente, será possível:

  - Escolher os produtos a partir de uma categoria selecionada;

  - Adicioná-los ao carrinho de compras;

  - Remover os itens já registrados até sobrar 1 pelo menos;

  - Diminuir a quantidade de um produto já registrado no pedido do cliente atual;

  - Cancelar a compra ao escolher a opção ou quando ocorrer a diminuição total da quantidade do último item restante do pedido;
  - Selecionar o método de pagamento.

## 🧑‍💼 Gerente
- Ao simular o gerente, será possível:

  - Adicionar novos produtos e clientes;

  - Alterar dados de clientes e produtos existentes;
    
  - Deletar dados de clientes e produtos existentes;
    
  - Deletar itens de pedidos já registrados;
    
  - Limpeza total da tabela de clientes, produtos e itenspedidos;

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
