-- Criação da tabela "Clientes"
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    data_cadastro DATE,
    status ENUM('ativo', 'inativo')
);

-- Inserção de um novo cliente na tabela
INSERT INTO Clientes (nome, email, data_cadastro, status)
VALUES ('Ana Silva', 'ana.silva@gmail.com', '2023-02-16', 'ativo');

-- Seleção do nome e email de todos os clientes ativos
SELECT nome, email
FROM Clientes
WHERE status = 'ativo';

-- Atualização do status do cliente com o email "ana.silva@gmail.com" para inativo
UPDATE Clientes
SET status = 'inativo'
WHERE email = 'ana.silva@gmail.com';

-- Exclusão de todos os clientes inativos da tabela
DELETE FROM Clientes
WHERE status = 'inativo';