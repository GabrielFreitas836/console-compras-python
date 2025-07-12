# 📦 Sobre o projeto

### Console de gerenciamento de compras feito em Visual Studio Code.
----
## ▶️ Como executar rapidamente

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/console-compras-python.git
```
2. Navegue até o diretório src:
```
cd console-compras-python/src
```
3. Crie um arquivo .env com as credenciais do seu banco.
  - Exemplo:
    ```
    DB_HOST = localhost
    DB_USER = seu_usuario
    DB_PASSWORD = sua_senha
    DB_DATABASE = nome_do_banco
    ```
4. Execute:
```
python main.py
```
----
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
## Conexão com o banco 
Dentro de src/config/ há um arquivo chamado conectar_banco.py e sua principal função é justamente criar a conexão com o banco MySQL:

```import mysql.connector


class ConectarBanco:
    
    def __init__(self):
        self.conn = None

    def conectar_ao_banco(self, bd_config):
        if self.conn is None or not self.conn.is_connected():
            self.bd_config = bd_config
            self.conn = mysql.connector.connect(**self.bd_config)
            print("Banco conectado com sucesso")
        else:
            pass
        return self.conn
    
    def fechar_conexao(self):
        if self.conn and self.conn.is_connected():
            print("Banco fechado com sucesso")
            self.conn.close()
```
O código acima define uma classe chamada ConectarBanco, responsável por gerenciar a conexão com o banco de dados MySQL. Esse módulo é essencial para centralizar e organizar o acesso ao banco de dados em todo o projeto.

✅ Principais funcionalidades:
 - Inicialização da classe (__init__)
   - Ao instanciar a classe, a conexão (self.conn) é inicialmente definida como None.

 - Método conectar_ao_banco(bd_config)

   - Estabelece uma conexão com o banco MySQL usando as configurações fornecidas (usuário, senha, host, banco de dados, etc.).

   - Verifica se já existe uma conexão ativa. Se não houver, conecta e exibe uma mensagem de sucesso.

   - Retorna o objeto de conexão (self.conn) para ser reutilizado em outras partes do código.

 - Método fechar_conexao(self)

   - Fecha a conexão com o banco caso ela esteja ativa.

   - Exibe uma mensagem informando que a conexão foi encerrada com sucesso.

💡 Benefícios:
 - Centraliza a lógica de conexão e desconexão em um único lugar.
 - Evita conexões duplicadas.
 - Facilita a manutenção e o reaproveitamento do código em diferentes módulos do projeto.
----
## Menu
  Este módulo é o coração da aplicação de gerenciamento de compras. Ele coordena o fluxo principal do programa e define o menu interativo para clientes e gerentes. A classe Menu funciona como ponto de entrada e controle das funcionalidades do sistema.

🔹 Importações
  - ConectarBanco: classe responsável por conectar ao banco de dados MySQL.

  - Cliente e Gerente: classes que encapsulam as interações e funcionalidades disponíveis para clientes e gerentes.

  - tabulate: usada para exibir os dados tabulados no terminal, facilitando a leitura de consultas SQL.

  - time: adiciona pequenas pausas para melhorar a experiência de visualização.

🧱 Classe Menu
 - 🔸 __init__(self)
   - Instancia objetos Cliente e Gerente. Isso prepara a aplicação para lidar com ambos os tipos de usuários.

 - 🔸 menu(bd_config)
   - Essa é a função principal da aplicação, chamada para iniciar o sistema. Aqui estão os passos principais:

   - Conexão com o banco de dados

   - Cria um novo objeto ConectarBanco e conecta usando as configurações fornecidas (bd_config).

   - A conexão é passada para os objetos Cliente e Gerente, permitindo que eles executem operações no banco.

 - Menu de seleção de perfil

   - O usuário escolhe entre:

     - [1] Cliente

     - [2] Gerente

     - [3] Sair do programa

🧾 Se o usuário for um Cliente:
 - O sistema tenta carregar os clientes registrados no banco.

 - Se não houver nenhum cliente, é oferecida a opção de registrar um novo.

 - Caso existam clientes, a lista é exibida de forma tabulada.

   - O usuário pode:

     - Registrar um novo cliente.

     - Escolher um cliente existente.

     - Encerrar a execução.

🧰 Se o usuário for um Gerente:
 - O método opcoes_gerente é chamado para apresentar e executar funcionalidades específicas de gerente (como gerenciar produtos, visualizar pedidos, etc.).

 - O menu se repete caso o gerente queira continuar.

 - A conexão é encerrada se ele optar por sair.

❌ Se o usuário escolher sair:
 - A conexão com o banco é encerrada.

 - O programa finaliza sua execução.

⚠️ Tratamento de entrada inválida:
 - Caso o usuário digite uma opção que não seja 1, 2 ou 3, o programa exibe uma mensagem de aviso e reinicia o menu principal após uma pequena pausa.
----
## Interação Gerente
 A classe Gerente reúne todas as ações administrativas do sistema. Através de um menu interativo, o gerente pode gerenciar clientes, produtos e pedidos diretamente no banco de dados.

 - 📋 Menu Principal
   - opcoes_gerente()
     - Exibe o menu principal com todas as opções disponíveis para o gerente. A partir dele, o usuário pode acessar e executar as funções administrativas do sistema.

 - 📌 Validações e Verificações
   - verificar_tabelas(tabela)
     - Verifica se uma tabela possui registros antes de realizar ações. Aceita apenas tabelas específicas: clientes, produtos, itens e pedidos.

 - ➕ Adição de Registros
   - adicionar_cliente()
     - Cadastra um novo cliente, solicitando informações como nome e idade

   - adicionar_produto()
     - Insere um novo produto no catálogo, com nome, valor unitário e categoria

 - ✏️ Atualização de Registros
   - atualizar_cliente()
     - Permite editar os dados de um cliente existente a partir do seu ID
     - Pode-se editar apenas o nome ou a idade ou os dois juntos

   - atualizar_produto()
     - Edita as informações de um produto já registrado
     - Pode-se editar as informações individualmente ou todas juntas

 - ❌ Remoção de Registros
    - deletar_cliente()
      - Exclui um cliente com base em seu ID.

    - deletar_produto()
      - Remove um produto específico informado pelo ID.

    - deletar_pedido()
      - Apaga um pedido existente do banco de dados.

 - 🧹 Limpeza Total de Tabelas
   - As funções abaixo removem todos os registros da respectiva tabela. Recomendado apenas em cenários de teste ou redefinição do sistema:

     - limpar_clientes

     - limpar_produtos

     - limpar_pedidos

### ⚠️ Atenção: Essas operações são irreversíveis. Use com cautela para não comprometer a integridade dos dados do sistema.
----
## Interação Cliente
 A classe Cliente representa o usuário final do sistema que irá realizar compras. Essa classe herda a conexão com o banco de dados da classe ConectarBanco e integra-se à classe Compras para registrar os itens comprados.

 - 📦 Estrutura da Classe
    - 🔄 Herança:
      - A classe Cliente herda de ConectarBanco, o que permite reutilizar os métodos de conexão com o banco.

      - Também instancia a classe Compras, responsável por gerenciar o carrinho e os pedidos feitos.

   - 🔍 Métodos disponíveis:
      - 🧩 __init__(conn=None)
        - Inicializa a instância do cliente.

        - Recebe uma conexão com o banco (conn) ou inicia sem conexão.

        - Cria também uma instância de Compras, passando a conexão para ela.

      - 📥 carregar_clientes(bd_config)
        - Consulta todos os clientes cadastrados na tabela clientes.

        - Armazena os resultados e os nomes das colunas para exibição com tabulate.

        - Usado para exibir a lista de clientes disponíveis no sistema.

      - 📝 registrar_cliente
        - Permite registrar um novo cliente, com nome e idade.

        - Trata duas situações:

          - Sem clientes no sistema: pergunta se o usuário deseja se registrar.

          - Com clientes já registrados: permite adicionar um novo cliente, mesmo com outros já existentes.

        - Após o registro, pode chamar automaticamente a função de seleção de cliente.

        - Inclui validação de entrada e mensagens guiadas para facilitar a navegação do usuário.

      - 🔐 escolher_cliente
        - Exibe a lista de clientes cadastrados e solicita ao usuário que selecione o seu ID.

        - Usa um loop while para garantir que a entrada seja válida.

        - Se o cliente for encontrado, chama a função adicionar_ao_carrinho() da classe Compras, iniciando o processo de compra.

 ### 🧠 Observações
  - A integração com a classe Compras permite associar diretamente um cliente a um pedido.

  - O uso de tabulate ajuda na visualização limpa dos dados diretamente no terminal.

  - O sistema é interativo e robusto para lidar com diferentes entradas e situações comuns.
----
## Controle de Compras
A classe Compras é responsável por gerenciar o processo de compra dos clientes, desde a escolha dos produtos até o pagamento, com suporte para alterações no carrinho, remoção de itens e cancelamento da compra

- 📦 Funções principais
  - 🔍 carregar_produtos(categoriaEscolhida)
     - Exibe os produtos disponíveis em uma categoria específica, utilizando menus interativos. Permite navegar entre as categorias e visualizar os itens de forma formatada.

  - 🛍️ adicionar_ao_carrinho(idcliente)
    - Fluxo completo de compra:

    - Seleciona produto e quantidade.

    - Verifica se o item já está no carrinho.

    - Insere ou atualiza registros na tabela itenspedidos.

    - Exibe o carrinho atualizado e oferece opções como:

       - Comprar mais
  
       - Remover item
  
       - Diminuir quantidade
  
       - Encerrar compra
  
       - Cancelar tudo

 - 📤 carregar_pedidos(idcliente)
    - Cria um novo pedido associado ao cliente atual, com um pagamento pendente (ID = 4).

 - 💳 pagamento(idcliente)
    - Apresenta o total da compra e solicita a forma de pagamento:

      - Dinheiro
      
      - Pix
      
      - Cartão (com entrada em débito ou parcelamento no crédito)

 - 💰 pagar_em_cartao(total)
    - Gera simulações de parcelamento dependendo do valor total:

      - Até 2x para compras pequenas
      
      - Até 12x para valores maiores

 - 🧾 atualizar_pagamento(idpagamento, idcliente)
    - Atualiza o método de pagamento escolhido na tabela pedidos.

 - 🧰 Ações sobre o Carrinho
    - ❌ remover_item(idcliente)
       - Permite remover itens específicos do carrinho via ID. Exibe todos os itens atuais do cliente e garante que ao menos um item permaneça no carrinho para manter a consistência.
    
    - ➖ diminuir_quantidade(idcliente, valorTotal)
       -  Diminui a quantidade de um item. Se a quantidade for zerada, o item é removido. Caso o carrinho fique vazio após a remoção, o pedido é automaticamente cancelado.
    
    - 🗑️ cancelar_compra(idcliente)
       - Pergunta ao usuário se ele deseja cancelar a compra. Se confirmado, remove todos os itens e o pedido correspondente do banco de dados.
    
  - 🧠 Observações
    - Todas as operações são protegidas com try/except para entradas inválidas.
    
    - O terminal interativo é amigável e orienta o usuário com mensagens e validações claras.
    
    - A integração com colorama, tabulate e time melhora a visualização, leitura e experiência do usuário.
  ----
  ## main.py
  O arquivo main.py é o início da execução do sistema. Ele é responsável por carregar a configuração do banco de dados, instanciar o menu principal e acionar a aplicação interativa de gerenciamento de compras.

  - 📌 Funcionalidades
  
    - Instancia a classe Menu:
    
      - Responsável por gerenciar as interações com clientes e gerentes.
    
      - Carrega variáveis de ambiente com dotenv:
      
      - Protege dados sensíveis como host, user, password e database, que são carregados de um arquivo .env.
      
    - Monta um dicionário de configuração (bd_config):
    
      - Passado para o sistema como parâmetro para que a conexão com o banco seja feita de forma dinâmica e segura.
      
    - Bloco try/except robusto:
    
      - Captura três tipos de erro:
    
        - mysql.connector.Error: erros de banco (como tabelas inexistentes, credenciais erradas etc.).
        
        - mysql.connector.InterfaceError: falhas de comunicação com o banco.
        
        - Exception: outros erros genéricos.
  
  - 🔒 Segurança
  
    - Este script usa a biblioteca python-dotenv para carregar variáveis do .env, impedindo que as credenciais do banco sejam expostas no código-fonte. Isso segue boas práticas de segurança em aplicações Python.
  ----
  ## 📺 Demonstração em vídeo

    Veja a aplicação rodando ao vivo no VS Code:

  👉 [Clique aqui para assistir no YouTube](https://youtube.com/seulink)
