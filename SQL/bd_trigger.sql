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
	nome_Aluno VARCHAR(30) NOT NULL,
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
	unid_Biblio SERIAL NOT NULL,
	quantCopias_Livro INT NOT NULL CHECK(quantCopias_Livro >= 1)
);

CREATE TYPE statusTipo AS ENUM ('Pago', 'Não Pago');
CREATE TABLE Empresta(
	id_Empresta SERIAL PRIMARY KEY,
	isbn_Empresta VARCHAR(20) NOT NULL,
	data_Emprestimo DATE NOT NULL CHECK(data_Emprestimo <= CURRENT_DATE),
	data_Prevista DATE NOT NULL CHECK(data_Prevista >= CURRENT_DATE),
	data_Retorno DATE NOT NULL CHECK(data_Retorno >= data_Emprestimo),
	matricAluno_Empresta VARCHAR(15) NOT NULL,
	multa REAL NOT NULL DEFAULT 0.0 CHECK(multa >= 0.0),
	status_Multa statusTipo NOT NULL
);

CREATE OR REPLACE FUNCTION emp_gatilho() RETURNS trigger AS $$
DECLARE
	emp INT := (SELECT COUNT(*) FROM Empresta WHERE matricAluno_Empresta = NEW.matricAluno_Empresta);
BEGIN
	IF emp > 4 THEN 
		RAISE EXCEPTION 'Aluno já possui 4 empréstimos.';
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
	('2020017295', '92784612235', 'Felipe Martins', 'Maria da Fé', DEFAULT), 
	('2019145362', '10918461942', 'Rosa Santos', 'São Paulo', DEFAULT),
	('2018047523', '10955185606', 'Gabriel Kenti', 'Itajubá', DEFAULT),
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
	('1512471242', 'La Casa de Papel', 3, '12/07/2000', '747718394100'),
	('8152569935', 'Mitologia Nórdica', 4, '02/12/2014', '994711312455'),
	('8693759832', 'Sniper Americano', 1, '04/05/2011', '354701645859'),
	('1315236274', 'Pequeno Príncipe', 2, '01/12/2013', '747718394100'),
	('4701042884', 'O Viajante do Tempo', 1, '12/02/2010', '354701645859'),
	('0560145468', 'Senhor dos Anéis', 5, '06/27/2011', '747718394100');

INSERT INTO empresta VALUES
	(DEFAULT, '8152569935', '09/10/2020', '09/10/2021', '11/04/2021', '2019000124', DEFAULT, 'Não Pago'),
	(DEFAULT, '1315236274', '09/10/2020', '09/10/2021', '11/04/2021', '2020001573', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2019042534', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2017095362', DEFAULT, 'Não Pago'),
	(DEFAULT, '1512471242', '09/10/2020', '09/10/2021', '11/04/2021', '2019145362', DEFAULT, 'Não Pago');

/* Para gerar o exception do trigger
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
	(DEFAULT, 'Biblioteca Danielle', 'Itajubá', '6245-4261');

INSERT INTO copias VALUES
	(DEFAULT, '1512471242', 1, 500),
	(DEFAULT, '8693759832', 1, 1500),
	(DEFAULT, '1512471242', 4, 3500),
	(DEFAULT, '0560145468', 2, 2500),
	(DEFAULT, '1512471242', 3, 1500),
	(DEFAULT, '8693759832', 1, 500);

INSERT INTO Autor VALUES
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
	




