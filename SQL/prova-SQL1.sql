/* Suponha que você é um desenvolvedor de uma empresa e precisa criar um banco de dados para armazenar informações de clientes e vendas. 


Preview
O banco de dados deve conter duas tabelas: Clientes e Vendas. A tabela Clientes deve conter as seguintes colunas: id (chave primária), nome, email e telefone. A tabela Vendas deve conter as seguintes colunas: id (chave primária), id_cliente (chave estrangeira referenciando a tabela Clientes), data e valor.

Sua resposta:
 */
 
CREATE DATABASE MinhaEmpresa;

USE MinhaEmpresa;

CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(15)
);

CREATE TABLE Vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    data DATE,
    valor DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);
