CREATE TABLE Autor(
	cpf_Autor VARCHAR(11) PRIMARY KEY,
	nome_Autor VARCHAR(30) NOT NULL UNIQUE,
	end_Autor VARCHAR(30) NOT NULL
);

CREATE TABLE Tel_Autor(
	tel_Autor VARCHAR(15) PRIMARY KEY,
	Autor VARCHAR(30) NOT NULL,
	FOREIGN KEY (Autor) REFERENCES Autor(cpf_Autor)
		ON UPDATE CASCADE
);

CREATE TABLE Editora(
	cnpj_Editora VARCHAR(20) PRIMARY KEY,
	nome_Editora VARCHAR(30) NOT NULL UNIQUE,
	end_Editora VARCHAR(30) NOT NULL
);

CREATE TABLE Tel_Editora(
	tel_Editora VARCHAR(15) PRIMARY KEY,
	Editora VARCHAR(20) NOT NULL,
	FOREIGN KEY (Editora) REFERENCES Editora(cnpj_Editora)
		ON UPDATE CASCADE
);

CREATE TABLE Livro(
	isbn_Livro VARCHAR(20) PRIMARY KEY,
	titulo_Livro VARCHAR(30) NOT NULL UNIQUE,
	edicao_Livro INT NOT NULL,
	anoEdicao_Livro DATE NOT NULL,
	editora_Livro VARCHAR(20) NOT NULL
	CHECK(anoEdicao_Livro >= '01/01/1991' AND anoEdicao_Livro <= CURRENT_DATE),
	FOREIGN KEY (editora_Livro) REFERENCES Editora(cnpj_Editora)
		ON UPDATE CASCADE
);

CREATE TABLE Biblioteca(
	unid_Biblio SERIAL PRIMARY KEY,
	nome_Biblio VARCHAR(30) UNIQUE,
	end_Biblio VARCHAR(30) NOT NULL,
	ramal_Biblio VARCHAR(15) NOT NULL
);

CREATE TYPE statusAluno AS ENUM ('Liberado', 'Bloqueado');
CREATE TABLE Aluno(
	matric_Aluno VARCHAR(15) PRIMARY KEY,
	cpf_Aluno VARCHAR(11) NOT NULL UNIQUE,
	nome_Aluno VARCHAR(30) NOT NULL UNIQUE,
	end_Aluno VARCHAR(30) NOT NULL,
	status statusAluno DEFAULT 'Liberado' NOT NULL 
);

CREATE TABLE Tel_Aluno(
	tel_Aluno VARCHAR(15) PRIMARY KEY,
	Aluno VARCHAR(15) NOT NULL,
	FOREIGN KEY (Aluno) REFERENCES Aluno(matric_Aluno)
		ON UPDATE CASCADE
);

CREATE TABLE Copias(
	id_Copia SERIAL PRIMARY KEY,
	isbn_Livro VARCHAR(20) NOT NULL,
	unid_Bib INT NOT NULL,
	quantCopias_Livro INT NOT NULL CHECK(quantCopias_Livro >= 1),
	FOREIGN KEY (unid_Bib) REFERENCES Biblioteca(unid_biblio)
		ON UPDATE CASCADE
);

CREATE TYPE statusTipo AS ENUM ('Pago', 'Não Pago');
CREATE TABLE Empresta(
	id_Empresta SERIAL PRIMARY KEY,
	isbn_Empresta VARCHAR(20) NOT NULL,
	data_Emprestimo DATE NOT NULL CHECK(data_Emprestimo <= CURRENT_DATE),
	data_Prevista DATE NOT NULL CHECK(data_Prevista >= CURRENT_DATE),
	data_Retorno DATE CHECK(data_Retorno >= data_Emprestimo),
	matricAluno_Empresta VARCHAR(15) NOT NULL,
	multa REAL NOT NULL DEFAULT 0.0 CHECK(multa >= 0.0),
	status_Multa statusTipo NOT NULL
);

CREATE TABLE Autor_Livro(
	Id_AutorLivro SERIAL PRIMARY KEY,
	Livro VARCHAR(20) NOT NULL,
	Autor VARCHAR(11) NOT NULL,
	FOREIGN KEY (Autor) REFERENCES Autor(cpf_autor)
		ON UPDATE CASCADE,
	FOREIGN KEY (Livro) REFERENCES Livro(isbn_livro)
		ON UPDATE CASCADE
);

-- TRIGGER verifica se aluno possui 4 devoluções pendentes para liberar a alocação do livro
CREATE OR REPLACE FUNCTION emp_gatilho() RETURNS trigger AS $$
DECLARE
	emp INT := (SELECT COUNT(*) 
					FROM 
						Empresta 
					WHERE 
						matricAluno_Empresta = NEW.matricAluno_Empresta AND
			   			CURRENT_DATE <= data_retorno);
BEGIN
	IF emp > 4 THEN 
		RAISE EXCEPTION 'Aluno já possui 4 empréstimos pendentes de entrega.';
	END IF;
	RETURN null;
END;      
$$ LANGUAGE plpgsql;

CREATE TRIGGER emp_gatilho AFTER INSERT ON Empresta
	FOR EACH ROW EXECUTE PROCEDURE emp_gatilho();

INSERT INTO aluno VALUES 
	('2019000124', '13204875738', 'Carlos José', 'Maria da Fé', DEFAULT), 
	('2019042534', '99817092315', 'Maria Antonieta', 'Três Corações', DEFAULT),
	('2020001573', '13208992445', 'Robson Camargo', 'Itajubá', DEFAULT),
	('2020018543', '48286648291', 'Samantha Silva', 'Maria da Fé', DEFAULT),
	('2020017295', '92784612235', 'Felipe Martins', 'Maria da Fé', 'Bloqueado'), 
	('2019145362', '10918461942', 'Rosa Santos', 'São Paulo', DEFAULT),
	('2018047523', '10955185606', 'Gabriel Kenti', 'Itajubá', 	'Bloqueado'),
	('2017095362', '54126542347', 'Roberto Gomes', 'Maria da Fé', DEFAULT);

INSERT INTO tel_aluno VALUES 
	('0432-1538', '2019042534'),
	('5418-9036', '2019042534'),
	('5367-7469', '2020018543'),
	('9058-8345', '2017095362'),
	('4883-4284', '2020018543'),
	('3964-2128', '2017095362'),
	('7903-1700', '2020001573'),
	('2793-8206', '2020001573'),
	('1898-6751', '2018047523');

INSERT INTO editora VALUES
	('747718394100', 'Pearson', 'São Paulo'),
	('994711312455', 'Records ltda.', 'São Paulo'),
	('354701645859', 'Leithura', 'Rio de Janeiro');

INSERT INTO tel_editora VALUES 
	('0432-1538', '747718394100'),
	('5334-1516', '747718394100'),
	('2617-4255', '354701645859'),
	('4267-4242', '994711312455');

INSERT INTO livro VALUES
	('7175464524', 'Iraq', 1, '04/05/2003', '354701645859'),
	('1512471242', 'La Casa de Papel', 3, '12/07/2000', '747718394100'),
	('8152569935', 'Mitologia Nórdica', 4, '02/12/2014', '994711312455'),
	('8693759832', 'Sniper Americano', 1, '04/05/2011', '354701645859'),
	('1315236274', 'Pequeno Príncipe', 2, '01/12/2013', '747718394100'),
	('4701042884', 'O Viajante do Tempo', 1, '12/02/2010', '354701645859'),
	('0560145468', 'Senhor dos Anéis', 5, '06/27/2011', '747718394100');

INSERT INTO empresta VALUES
	(DEFAULT, '1315236274', '12/01/2020', '12/06/2021', '12/07/2020', '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '8152569935', '01/07/2020', '01/07/2021', '11/12/2020', '2019145362', DEFAULT, 'Não Pago'),
	(DEFAULT, '0560145468', '01/07/2020', '01/07/2021', NULL, '2019145362', DEFAULT, 'Não Pago'),
	(DEFAULT, '8152569935', '09/10/2020', '09/10/2021', NULL, '2020017295', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '11/25/2020', '11/25/2021', '12/01/2020', '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '8152569935', '11/25/2020', '11/25/2021', '12/01/2020', '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '8693759832', '11/25/2020', '11/25/2021', NULL, '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '1315236274', '11/25/2020', '11/25/2021', '12/01/2020', '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '4701042884', '11/25/2020', '11/25/2021', NULL, '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '0560145468', '11/25/2020', '11/25/2021', NULL, '2018047523', DEFAULT, 'Não Pago'),
	(DEFAULT, '0560145468', '09/10/2020', '09/10/2021', NULL, '2020017295', DEFAULT, 'Não Pago'),
	(DEFAULT, '8152569935', '01/01/2020', '01/01/2021', '03/22/2020', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1315236274', '11/04/2020', '11/04/2021', NULL, '2020001573', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '05/05/2020', '05/05/2021', '02/14/2021', '2019042534', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '07/03/2020', '07/03/2021', NULL, '2017095362', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '01/07/2020', '01/07/2021', NULL, '2019145362', DEFAULT, 'Não Pago');

/* PARA GERAR O EXCEPTION DO TRIGGER

INSERT INTO Empresta VALUES
	(DEFAULT, '8152569935', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1315236274', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago');
*/

INSERT INTO biblioteca VALUES
	(DEFAULT, 'Biblioteca Mauá', 'UNIFEI', '1827-1731'),
	(DEFAULT, 'Bilioteca Leia Bem', 'Santa Catarina', '1534-1734'),
	(DEFAULT, 'Bilbioteca Mariense', 'Maria da Fé', '3662-1503'),
	(DEFAULT, 'Biblioteca Danielle', 'Itajubá', '6245-4261'),
	(DEFAULT, 'Biblioteca Itajubense', 'Itajubá', '6234-1131');

INSERT INTO copias VALUES
	(DEFAULT, '1512471242', 4, 3500),
	(DEFAULT, '0560145468', 2, 2500),
	(DEFAULT, '4701042884', 3, 1500),
	(DEFAULT, '1512471242', 3, 1500),
	(DEFAULT, '8693759832', 1, 500),
	(DEFAULT, '1512471242', 5, 500),
	(DEFAULT, '8693759832', 1, 1500);

INSERT INTO Autor VALUES
	('61753758312', 'Tarin Akayama', 'Tokyo'),
	('20194170504', 'John Stewart', 'Chicago'),
	('18374687931', 'Ivan Tapia', 'Belo Horizonte'),
	('84647398021', 'Neil Gaiman', 'Fortaleza'),
	('74636183912', 'Chris Kyle', 'Recife'),
	('94736820861', 'Antoine de Saint-Exupéry', 'São Paulo'),
	('28376437821', 'Edson Cordeiro', 'Rio de Janeiro'),
	('83649627612', 'J. R. R. Tolkien', 'Itajubá');
	
INSERT INTO tel_autor VALUES
	('1412-1755', '18374687931'),
	('1245-6132', '84647398021'),
	('6134-1675', '84647398021'),
	('4123-1634', '83649627612'),
	('2294-1771', '74636183912');

INSERT INTO Autor_Livro VALUES
	(DEFAULT, '7175464524', '74636183912'),
	(DEFAULT, '1512471242', '18374687931'),
	(DEFAULT, '8152569935', '84647398021'),
	(DEFAULT, '8693759832', '74636183912'),
	(DEFAULT, '1315236274', '94736820861'),
	(DEFAULT, '4701042884', '28376437821'),
	(DEFAULT, '0560145468', '83649627612');

-- Retorne o nome do aluno, o título do livro emprestado e o(s) nome(s) do(s) 
-- atores considerando somente os alunos que estão com status Bloqueado
SELECT a.nome_aluno, li.titulo_livro, au.nome_autor 
	FROM 
		aluno a, 
		empresta e, 
		livro li, 
		autor_livro auL, 
		autor au 
	WHERE  
		e.matricaluno_empresta = a.matric_aluno AND
		e.isbn_empresta = li.isbn_livro AND
		au.cpf_autor = auL.autor AND
		auL.livro = li.isbn_livro AND
		a.status = 'Bloqueado'
		
-- Retorne o nome dos alunos que tomaram todos os livros cadastrados emprestados.
SELECT a.nome_aluno 
	FROM 
		aluno a
	WHERE 
		(SELECT COUNT(DISTINCT e.isbn_empresta) 
		 	FROM 
		 		empresta e 
		 	WHERE 
		 		e.matricaluno_empresta = a.matric_aluno) = (SELECT COUNT(*) FROM livro)

-- Retorne o nome da biblioteca e a quantidade de cópias 
-- considerando somente as bibliotecas que possuem mais que 500 cópias
SELECT b.nome_biblio, SUM(cp.quantcopias_livro)
	FROM 
		biblioteca b,
		copias cp
	WHERE
		cp.quantcopias_livro > 500 AND
		b.unid_biblio = cp.unid_bib
	GROUP BY (b.nome_biblio)

-- Suponha que existam autores que não estejam associados a algum livro, retorne o nome do autor, 
-- o título dos livros publicados e o nome da editora considerando inclusive os autores que não 
-- estão associados a algum livro.
SELECT au.nome_autor, li.titulo_livro, ed.nome_editora
	FROM Autor au 
		LEFT JOIN autor_livro AuL ON au.cpf_autor = AuL.autor 
		LEFT JOIN Livro li ON Aul.livro = li.isbn_livro
		LEFT JOIN Editora ed ON li.editora_livro = ed.cnpj_editora

		

-- Procedure retorna livro baseado no ISBN, Título ou Autor
CREATE OR REPLACE FUNCTION consulta_tipo(tipo INT, cod VARCHAR(30)) 
RETURNS Livro 
AS $$
DECLARE Livr Livro%ROWTYPE;
BEGIN
	IF tipo = 1 THEN 
		SELECT * INTO Livr FROM Livro WHERE isbn_livro = cod;
	ELSIF tipo = 2 THEN
		SELECT * INTO Livr FROM Livro WHERE titulo_livro = cod;
	ELSE
		SELECT * INTO Livr FROM Livro li, Autor_Livro al, Autor au 
			WHERE al.livro = li.isbn_livro AND
				  al.autor = au.cpf_autor AND
				  au.nome_autor = cod;
	END IF;
	RETURN Livr;
END;      
$$ LANGUAGE plpgsql;

SELECT consulta_tipo(1, '1512471242')
SELECT consulta_tipo(2, 'Senhor dos Anéis')
SELECT consulta_tipo(3, 'Chris Kyle')

CREATE OR REPLACE FUNCTION devolvelivro2() RETURNS trigger
AS $$
DECLARE
	Data_Prev DATE := (SELECT data_prevista FROM empresta a WHERE a.id_empresta = NEW.id_empresta);
	Dias INT := (CURRENT_DATE - Data_Prev);
BEGIN
	IF Dias > 0 THEN
		UPDATE empresta
			SET multa = Dias * 1.0
			WHERE id_empresta = NEW.id_empresta;
	END IF;
	RETURN null;
END;
$$ LANGUAGE plpgsql;

-- Trigger só é ativado se haver alteração na coluna 'data_retorno' de Empresta 
CREATE TRIGGER devolvelivro2 AFTER UPDATE OF data_retorno ON empresta 
	FOR EACH ROW EXECUTE PROCEDURE devolvelivro2();
	
	
CREATE MATERIALIZED VIEW emprestimolivroaluno AS SELECT
Aluno.nome_Aluno AS "Aluno", Livro.titulo_Livro AS "Livro", Emp.data_Prev
ista AS "Previsao entrega", Emp.data_Retorno AS "Data de Retorno", Emp.mu
lta AS "Multa"
FROM Empresta AS Emp
	INNER JOIN Livro AS Livro
		ON livro.isbn_Livro = Emp.isbn_Empresta
	INNER JOIN Aluno AS Aluno
		ON Aluno.matric_Aluno = Emp.matricAluno_Empresta;

