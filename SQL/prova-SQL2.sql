CREATE DATABASE Escola;

USE Escola;

CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE
);

CREATE TABLE Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    disciplina VARCHAR(255) NOT NULL,
    nota DECIMAL(5, 2),
    FOREIGN KEY (id_aluno) REFERENCES Alunos(id)
);
