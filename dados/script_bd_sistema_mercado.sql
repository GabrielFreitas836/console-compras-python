-- Criando o banco 'sistema_mercado'
CREATE DATABASE IF NOT EXISTS sistema_mercado;

-- Colocando o sistema em uso
USE sistema_mercado;

-- Criando as tabelas essenciais do banco
CREATE TABLE IF NOT EXISTS clientes (
	idCliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45),
    idade INT
);

CREATE TABLE IF NOT EXISTS pagamento (
	idPagamento INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS categorias (
	idCategoria INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS produtos (
	idProduto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(60),
    valorUnitario DECIMAL(10, 2),
    categoria_idCategoria INT NOT NULL,
    FOREIGN KEY (categoria_idCategoria) REFERENCES categorias(idCategoria)
);

CREATE TABLE IF NOT EXISTS pedidos (
	idPedido INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cliente_idCliente INT NOT NULL,
    pagamento_idPagamento INT NOT NULL,
    FOREIGN KEY (cliente_idCliente) REFERENCES clientes(idCliente),
    FOREIGN KEY (pagamento_idPagamento) REFERENCES pagamento(idPagamento)
);

CREATE TABLE IF NOT EXISTS itenspedidos (
	idItens INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    quantidade INT,
    produto_idProduto INT NOT NULL,
    pedido_idPedido INT NOT NULL,
    valorTotal DECIMAL(10, 2),
    FOREIGN KEY (produto_idProduto) REFERENCES produtos(idProduto),
    FOREIGN KEY (pedido_idPedido) REFERENCES pedidos(idPedido)
);