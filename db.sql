DROP SCHEMA IF EXISTS ferragem;
CREATE SCHEMA IF NOT EXISTS ferragem;
USE ferragem;
SET default_storage_engine=INNODB;

CREATE TABLE ufs (
  id INT NOT NULL,
  sigla CHAR(2) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE cidades (
  id INT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  ufs_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_cidades_ufs
    FOREIGN KEY (ufs_id) REFERENCES ufs (id));

CREATE TABLE clientes (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  email VARCHAR(120) NOT NULL,
  senha VARCHAR(32) NOT NULL,
  telefone VARCHAR(11) NULL,
  endereco_tipo VARCHAR(20) NULL,
  endereco_logradouro VARCHAR(100) NULL,
  endereco_numero VARCHAR(20) NULL,
  endereco_complemento VARCHAR(60) NULL,
  endereco_bairro VARCHAR(100) NULL,
  cidades_id INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (email),
  CONSTRAINT fk_clientes_cidades
    FOREIGN KEY (cidades_id) REFERENCES cidades (id));

CREATE TABLE carrinhos (
  id INT(11) NOT NULL AUTO_INCREMENT,
  data DATETIME NOT NULL,
  valor_total FLOAT NOT NULL,
  desconto FLOAT NOT NULL,
  id_cliente INT(11) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT carrinhos_clientes
    FOREIGN KEY (id_cliente) REFERENCES clientes (id));

CREATE TABLE categorias (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(30) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE fornecedores (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  cnpj VARCHAR(14) NOT NULL,
  telefone VARCHAR(15) NOT NULL,
  email VARCHAR(60) NOT NULL,
  representante VARCHAR(30) NOT NULL,
  telefone_representante VARCHAR(15) NOT NULL,
  email_representante VARCHAR(60) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE marcas (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(30) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE pedidos (
  id INT(11) NOT NULL AUTO_INCREMENT,
  data_compra DATETIME NOT NULL,
  data_entrega DATETIME NOT NULL,
  id_cliente INT(11) NOT NULL,
  desconto FLOAT NULL,
  valor FLOAT NULL,
  PRIMARY KEY (id),
  CONSTRAINT pedidos_clientes
    FOREIGN KEY (id_cliente) REFERENCES clientes (id));

CREATE TABLE produtos (
  id INT(11) NOT NULL AUTO_INCREMENT,
  data_compra DATETIME NOT NULL,
  nome VARCHAR(200) NOT NULL,
  descricao VARCHAR(200) NULL,
  imagem VARCHAR(300) NULL,
  unidade VARCHAR(2) NOT NULL,
  quant INT(11) NOT NULL,
  quant_minima INT(11) NOT NULL,
  valor_compra FLOAT NOT NULL,
  porcentagem INT(11) NOT NULL,
  valor_venda FLOAT NOT NULL,
  peso FLOAT NULL,
  fornecedor_id INT(11) NOT NULL,
  marca_id INT(11) NOT NULL,
  categoria_id INT(11) NOT NULL,
  destaque VARCHAR(1) NULL,
  PRIMARY KEY (id),
  CONSTRAINT produtos_fornecedores
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores (id),
  CONSTRAINT produtos_marcas
    FOREIGN KEY (marca_id) REFERENCES marcas (id),
  CONSTRAINT produtos_categorias
    FOREIGN KEY (categoria_id) REFERENCES categorias (id));

CREATE TABLE usuarios (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  email VARCHAR(120) NOT NULL,
  senha VARCHAR(32) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (email));

CREATE TABLE pedidos_produtos (
  pedidos_id INT(11) NOT NULL,
  produtos_id INT(11) NOT NULL,
  quantidade INT NULL,
  desconto FLOAT NULL,
  valor FLOAT NULL,
  PRIMARY KEY (pedidos_id, produtos_id),
  CONSTRAINT fk_pedidos_produtos1
    FOREIGN KEY (pedidos_id) REFERENCES pedidos (id),
  CONSTRAINT fk_pedidos_produtos2
    FOREIGN KEY (produtos_id) REFERENCES produtos (id));

CREATE TABLE carrinhos_produtos (
  carrinhos_id INT(11) NOT NULL,
  produtos_id INT(11) NOT NULL,
  quantidade INT NULL,
  desconto FLOAT NULL,
  valor FLOAT NULL,
  PRIMARY KEY (carrinhos_id, produtos_id),
  CONSTRAINT fk_carrinhos_produtos
    FOREIGN KEY (produtos_id) REFERENCES produtos (id));
