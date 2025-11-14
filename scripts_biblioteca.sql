-- Criação do banco de dados
-- CREATE DATABASE IF NOT EXISTS biblioteca2;
-- USE biblioteca2;

-- Tabela de estudantes
-- CREATE TABLE estudantes (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     cpf VARCHAR(14) NOT NULL UNIQUE,
--     nome VARCHAR(100) NOT NULL
-- );

-- Tabela de livros
-- CREATE TABLE livros (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     isbn VARCHAR(20) NOT NULL UNIQUE,
--     titulo VARCHAR(150) NOT NULL
-- );

-- Tabela de empréstimos
-- CREATE TABLE emprestimo (
--     id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
--     data_emp DATE NOT NULL,
--     id_estudante INT NOT NULL,
--     id_livro INT NOT NULL,
--     FOREIGN KEY (id_estudante) REFERENCES estudantes(id),
--     FOREIGN KEY (id_livro) REFERENCES livros(id)
-- );

-- Inserção de estudantes
-- INSERT INTO estudantes (cpf, nome) VALUES
-- ('123.456.789-00', 'Ana Souza'),
-- ('987.654.321-11', 'Bruno Lima'),
-- ('456.789.123-22', 'Carla Mendes'),
-- ('321.654.987-33', 'Diego Martins'),
-- ('159.753.486-44', 'Eduarda Ribeiro');

-- Inserção de livros
-- INSERT INTO livros (isbn, titulo) VALUES
-- ('978-85-359-0277-8', 'Dom Casmurro'),
-- ('978-85-359-0301-0', 'O Cortiço'),
-- ('978-85-325-1234-5', '1984'),
-- ('978-85-325-6789-0', 'A Revolução dos Bichos'),
-- ('978-85-359-0400-0', 'O Pequeno Príncipe');

-- Inserção de empréstimos
-- INSERT INTO emprestimo (data_emp, id_estudante, id_livro) VALUES
-- ('2025-11-01', 1, 3),
-- ('2025-11-02', 2, 1),
-- ('2025-11-03', 3, 5),
-- ('2025-11-04', 4, 2),
-- ('2025-11-05', 5, 4);

use biblioteca2;

-- 1 - Liste todos os empréstimos feitos pelo estudante com id_estudante = 3
-- SELECT * FROM emprestimo
-- where id_estudante = 3;

-- 2 - Liste todos os empréstimos realizados após o dia 2025-11-02
-- select * from emprestimo
-- where data_emp > '2025-11-02';

-- 3 - Encontre todos os estudantes cujo nome começa com a letra 'C' utilizando '%' pra encontrar a letra, tipo 'C%' buscar C na frente.
-- select * from estudantes
-- where nome like 'C%'; 

-- 4 - Liste os livros cujo id está entre os valores 1, 3 e 5. (verificar como esta as colunas para a pesquisa dar certo.)
-- select * from livros
-- where id in (1,3,5);

-- 5 - Liste os empréstimos realizados entre 2025-11-02 e 2025-11-04
-- select * from emprestimo
-- where data_emp between '2025-11-02' and '2025-11-04';

-- 6 - Conte quantos empréstimos existem no total. criemos uma coluna temporaria pro resultado = 'total_emprestimos'
-- select count(*) as total_emprestimos
-- from emprestimo;

-- 7 - Mostre quantos empréstimos cada estudante realizou.
-- select id_estudante, count(*) as total_emprestimos
-- from emprestimo
-- group by id_estudante;

-- 8 - Liste apenas os estudantes que fizeram mais de 1 empréstimo, utilizando HAVING
-- select id_estudante, count(*) as total_emprestimos
-- from emprestimo
-- group by id_estudante
-- having count(*) > 1;

-- 9 - Mostre uma lista com o nome do estudante, o título do livro e a data do empréstimo. JOIN (INNER JOIN)
-- atenção nos nomes das colunas, esse 'as' pode adicionar um 'apelido' a tabela relacionada.
-- select
-- 	estudantes.nome as nome_estudante,
--     livros.titulo as titulo_livro,
--     emprestimo.data_emp
-- from emprestimo
-- inner join estudantes on emprestimo.id_estudante = estudantes.id
-- inner join livros on emprestimo.id_livro = livros.id;

-- 10 - Liste os empréstimos em que o nome do estudante contém a letra 'a' e o título do livro começa com 'O'
-- utilize: JOIN + WHERE + LIKE
-- select
-- 	estudantes.nome as n_estudante,
--     livros.titulo as t_livro,
--     emprestimo.data_emp
-- from emprestimo
-- inner join estudantes on emprestimo.id_estudante = estudantes.id
-- inner join livros on emprestimo.id_livro = livros.id
-- where estudantes.nome like '%a%' and livros.titulo like 'O%';